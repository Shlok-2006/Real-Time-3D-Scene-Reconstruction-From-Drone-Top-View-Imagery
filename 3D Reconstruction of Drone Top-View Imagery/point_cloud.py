import numpy as np
import open3d as o3d
import cv2
import os


# ---------------------------
# CONFIG
# ---------------------------
FX = 640
FY = 640
DEPTH_SCALE = 5.0

VIEW_ROTATIONS = {
    "front": 0,
    "right": 90,
    "back": 180,
    "left": 270
}


def load_depth(path):
    d = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if d is None:
        return None

    if len(d.shape) == 3:
        d = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)

    return d.astype(np.float32) / DEPTH_SCALE


def make_point_cloud(rgb_path, depth_path, yaw_deg):
    depth = load_depth(depth_path)
    if depth is None:
        print("Missing depth:", depth_path)
        return None

    rgb = cv2.imread(rgb_path)
    if rgb is None:
        print("Missing image:", rgb_path)
        return None

    depth = np.squeeze(depth)
    h, w = depth.shape

    rgb = cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB)
    rgb = cv2.resize(rgb, (w, h))

    cx, cy = w / 2, h / 2

    points = []
    colors = []

    for y in range(h):
        for x in range(w):
            Z = depth[y, x]
            if Z <= 0:
                continue

            X = (x - cx) * Z / FX
            Y = (y - cy) * Z / FY

            points.append([X, -Y, Z])
            colors.append(rgb[y, x] / 255.0)

    pc = o3d.geometry.PointCloud()
    pc.points = o3d.utility.Vector3dVector(np.array(points))
    pc.colors = o3d.utility.Vector3dVector(np.array(colors))

    yaw = np.deg2rad(yaw_deg)
    R = pc.get_rotation_matrix_from_xyz((0, yaw, 0))
    pc.rotate(R, center=(0, 0, 0))

    return pc


def merge_sides():
    final_pc = o3d.geometry.PointCloud()

    for name, yaw in VIEW_ROTATIONS.items():
        rgb = os.path.join("input_images", f"{name}.jpg")
        depth = os.path.join("depth_outputs", f"{name}_depth.png")

        if not os.path.exists(rgb):
            print("Missing RGB:", rgb)
            continue
        if not os.path.exists(depth):
            print("Missing Depth:", depth)
            continue

        print("Processing:", name)

        pc = make_point_cloud(rgb, depth, yaw)
        if pc is None:
            continue

        final_pc += pc

    if len(final_pc.points) == 0:
        print("ERROR: No point clouds created!")
        return

    centroid = final_pc.get_center()
    final_pc.translate(-centroid)

    final_pc = final_pc.voxel_down_sample(0.03)

    o3d.io.write_point_cloud("pc.ply", final_pc)
    print("Saved: pc.ply")

    o3d.visualization.draw_geometries([final_pc])


merge_sides()
