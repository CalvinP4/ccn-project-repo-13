# **Visual Speech-Aware Perceptual 3D Facial Expression Reconstruction from Videos**

## **Table of Contents**
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Team Members](#team-members)

---

## **Introduction**
For ITCS-6166, we selected **Spectre** as our exploratory project and successfully ran it on a local system.

This project introduces a novel method for perceptual 3D reconstruction of facial expressions, especially during speech, from video footage. Using advancements in deep learning, it addresses limitations in existing monocular 3D face reconstruction methods, particularly in rendering accurate mouth movements. A key innovation is the introduction of a "lipread" loss function, enabling the reconstructed 3D facial models to closely mimic the input video, especially around the mouth area. Unlike traditional methods, this approach requires neither text transcriptions nor audio data, making it ideal for training on unlabeled datasets.

### **Applications**  
The technology has a wide range of applications, including:
- **Augmented Reality (AR)**  
- **Performance Capture**  
- **Visual Effects**  
- **Photo-Realistic Video Synthesis**  
- **Human-Computer Interaction**  
- **Personalized Avatars**  

By preserving speech perception in 3D reconstructions, the project contributes significantly to natural and realistic digital human representations.

---

## **Prerequisites**

Ensure the following software and libraries are installed:

### **Core Requirements**
- **Python 3.8+**: [Download Python](https://www.python.org/)
- **pip**: Comes with Python; install via `get-pip.py` if needed.

### **Python Libraries**
Install the libraries below using `pip install <library_name>`:
- `numpy`
- `pandas`
- `scikit-learn`
- `torch` (PyTorch)
- `opencv-python` (OpenCV)
- `dlib`
- `face-alignment`
- `matplotlib`

### **Additional Requirements**
- **CUDA Toolkit 11.8** (for GPU support): [Download CUDA](https://developer.nvidia.com/cuda-downloads)
- **C++ Build Tools** (required for building PyTorch3D on Windows)

---

## **Installation**

Follow these steps to set up the project locally:

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2.  **Set Up Virtual Environment**
   ```bash
  python -m venv env
  source env/bin/activate  # On Windows: `env\Scripts\activate`
  ```

3. **Install Dependencies**
  ```bash
  pip install -r requirements.txt
  ```

4. **Install CUDA Toolkit 11.8**
  Download and install the appropriate version from NVIDIA's website.

5. **Build PyTorch3D from Source (Windows)**
   ```bash
    git clone https://github.com/facebookresearch/pytorch3d.git
    cd pytorch3d
    pip install -r requirements.txt
    python setup.py install
   ```

---

## **Usage**

1. **Start the Application**
   After setting up the project, launch the app:
   ```bash
   python app.py
   ```

2. **Upload Video for Processing**
   - Open the app in a browser at `http://localhost:5000`.
   - Enter the path to a `.mp4` video file and click Run Model.
  
3. **View the Results**
   The model will output two videos:
   - A 3D reconstructed model
   - A side-by-side comparison of the 3D model with a grid
  
---

## **Project Structure**

1. **User Interaction:** The app provides a browser-based interface for user input.
2. **Backend Server:** A Flask server processes requests and interfaces with Spectre via a command-line interface.

### Architecture Overview
Below is a conceptual representation of the system architecture:
![image](https://github.com/user-attachments/assets/4ee8400a-d6ac-4ff9-a98c-3d4aaa845cb0)



  
