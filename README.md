# Real-Time-3D-Scene-Reconstruction-From-Drone-Top-View-Imagery
**🥉 3rd Prize Winner – Hackathon Project**

## 📌 Overview
This project focuses on reconstructing a 3D model from multiple 2D RGB images using AI-based depth estimation. By leveraging the **Depth Anything V2** model, images captured from different viewpoints (front, right, back, left) are converted into depth maps, fused into a unified 3D point cloud, and reconstructed into a smooth 3D mesh.

This project won **3rd Prize** in a competitive hackathon for its innovative application of computer vision and 3D reconstruction techniques.

---

## 🚀 Features
- Multi-view 360° 3D reconstruction
- AI-based depth estimation using Depth Anything V2
- RGB + Depth to Point Cloud conversion
- Point cloud alignment and fusion
- Poisson surface reconstruction
- Exportable `.ply` and `.obj` files
- Fully offline 3D processing pipeline

---

## 🛠️ Tech Stack
- **Programming Language:** Python
- **AI Model:** Depth Anything V2
- **Computer Vision:** OpenCV
- **3D Processing:** Open3D
- **Numerical Computation:** NumPy

---

## ▶️ How to Run the Project

### 1️⃣ Install Required Dependencies
    ```bash
    pip install numpy open3d opencv-python pillow transformers torch

### 2️⃣ Prepare Input Images
    ```bash
    input_images/
- Supported formats: .jpg, .jpeg, .png, .webp

### 3️⃣ Generate Depth Maps
    ```bash
    python depth_estimation.py
- Depth maps will be saved in:
    ```bash
    depth_outputs/

### 4️⃣ Generate 3D Point Cloud
    ```bash
    python point_cloud.py
- Output:
    ```bash
    pc.ply

### 5️⃣ Reconstruct 3D Mesh
    ```bash
    python mesh_reconstruction.py
- Output:
     ```bash
     3d_model.obj

---

## 🧠 Pipeline Overview

1. **Input RGB Images**  
   - Images captured from multiple viewpoints (front, right, back, left)

2. **Depth Estimation**  
   - Depth maps generated using **Depth Anything V2**

3. **Point Cloud Generation**  
   - Depth + camera intrinsics used to compute 3D coordinates

4. **View Alignment & Fusion**  
   - Multiple views rotated and merged into a single point cloud

5. **Mesh Reconstruction**  
   - Poisson surface reconstruction for smooth 3D mesh generation

6. **Export & Visualization**  
   - Final outputs saved as `.ply` and `.obj` files

---

## 📌 Applications

- 3D Scene Reconstruction
- Drone and Aerial Imagery
- Robotics and Autonomous Perception
- AR / VR Environment Generation
- Digital Twin Creation
- 3D Asset Generation
- Smart City and Mapping Applications

