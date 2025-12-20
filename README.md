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

## 🧠 Pipeline Overview
1. Input RGB images captured from multiple viewpoints  
2. Depth estimation using Depth Anything V2  
3. 3D point cloud generation using depth and camera intrinsics  
4. View alignment and point cloud fusion  
5. Poisson surface reconstruction for mesh generation  
6. Export and visualization of final 3D model

---

##📌 Applications
-3D scene reconstruction
-AR / VR environments
-Robotics and perception
-Digital twin creation
-Drone and aerial imaging
-3D asset generation
