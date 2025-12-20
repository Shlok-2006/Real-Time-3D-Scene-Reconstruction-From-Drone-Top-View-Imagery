import open3d as o3d

pc = o3d.io.read_point_cloud("pc.ply")
pc = pc.voxel_down_sample(voxel_size=0.02)
pc.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.05, max_nn=30))

mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pc, depth=10)
mesh = mesh.filter_smooth_taubin(number_of_iterations=50)

o3d.io.write_triangle_mesh("3d_model.obj", mesh)
o3d.visualization.draw_geometries([mesh])