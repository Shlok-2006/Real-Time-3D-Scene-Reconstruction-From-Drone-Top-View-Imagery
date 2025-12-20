from PIL import Image
import numpy as np
import cv2
import os
from transformers import pipeline

# ---------------------------------------------------------
# CONFIG
# ---------------------------------------------------------
input_folder = "input_images"       # folder containing your images
output_folder = "depth_outputs"     # folder where depth maps will be saved

os.makedirs(output_folder, exist_ok=True)

print("Loading DepthAnything V2 model...")
pipe = pipeline(
    task="depth-estimation",
    model="depth-anything/Depth-Anything-V2-Small-hf"
)

valid_exts = [".jpg", ".jpeg", ".png", ".webp"]

# ---------------------------------------------------------
# PROCESS EACH IMAGE
# ---------------------------------------------------------
for filename in os.listdir(input_folder):
    if not any(filename.lower().endswith(ext) for ext in valid_exts):
        continue

    img_path = os.path.join(input_folder, filename)
    print(f"\nProcessing image: {img_path}")

    try:
        img = Image.open(img_path).convert("RGB")
    except:
        print(f"Could not load {img_path}")
        continue

    result = pipe(img)

    depth_pil = result["depth"]
    depth = np.array(depth_pil).astype("float32")

    # Normalize
    depth = depth - depth.min()
    if depth.max() > 0:
        depth = depth / depth.max()

    depth_vis = (depth * 255).astype("uint8")

    # Output file
    name, ext = os.path.splitext(filename)
    out_path = os.path.join(output_folder, f"{name}_depth.png")

    cv2.imwrite(out_path, depth_vis)

    print(f"Saved depth map: {out_path}")

print("\n------------------------------------------")
print("Depth estimation complete for all images!")
print(f"Output folder: {output_folder}")
print("------------------------------------------")
