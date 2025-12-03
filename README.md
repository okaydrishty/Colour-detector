---

# 🎨 **Colour Detector – Project Description**

The **Colour Detector** is a computer vision project that identifies and highlights specific colours in real-time using a webcam feed. By converting the video frames from **BGR to HSV colour space**, the system creates a colour range (lower and upper limits) and filters out everything except the selected colour.

The project uses **OpenCV** to continuously capture frames, apply a mask based on the chosen colour, and display the detected region clearly. It is useful for applications like object tracking, gesture control, robotics, and visual filtering.

---

## 🔧 **Key Features**

* Real-time webcam video processing
* Detects any user-defined colour using HSV ranges
* Dynamic colour range calculation for accurate detection
* Highlights and isolates the selected colour
* Works smoothly even under varying lighting conditions

---

## 🧠 **How It Works**

1. Capture webcam frame using OpenCV
2. Convert frame from **BGR → HSV**
3. Generate **lower and upper HSV limits** from the target colour
4. Apply `cv2.inRange()` to create a mask
5. Extract and display only the detected colour region

---

## 💡 **Technologies Used**

* Python
* OpenCV (cv2)
* NumPy

---

## 📌 **Applications**

* Object and colour-based tracking
* Robotics and automation
* Traffic signal and object colour detection
* Interactive AI/ML projects
* Educational computer vision demos

---

