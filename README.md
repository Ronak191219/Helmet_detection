# 🪖 Helmet Detection System using YOLOv8

## 📌 Overview

This project is a **Computer Vision-based Helmet Detection System** that detects whether a person is wearing a helmet or not using a trained **YOLOv8 model**.

It can be used in real-world scenarios such as:

* Traffic monitoring 🚦
* Road safety enforcement 👮
* Smart surveillance systems 📹

---

## 🚀 Features

* Real-time helmet detection
* Built using YOLOv8 (Ultralytics)
* Streamlit-based interactive UI
* Custom-trained model
* Image upload support

---

## 🏗️ Project Architecture

```
User Input (Image)
        ↓
Streamlit Frontend (app.py)
        ↓
YOLOv8 Model (best.pt)
        ↓
Object Detection
        ↓
Result Display (Helmet / No Helmet)
```

---

## 📂 Project Structure

```
Helmet_detection/
│── app.py              # Streamlit app (frontend)
│── train.py            # Model training script
│── fix_label.py        # Dataset label preprocessing
│── data.yaml           # Dataset configuration
│── README.md           # Project documentation
│── requirements.txt    # Dependencies
│── .gitignore          # Ignore unnecessary files
```

---

## 🧠 Tech Stack

* Python 🐍
* YOLOv8 (Ultralytics)
* Streamlit
* OpenCV
* NumPy
* PIL

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/Helmet_detection.git
cd Helmet_detection
```

### 2️⃣ Create virtual environment (optional but recommended)

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
streamlit run app.py
```

Then open in browser:

```
http://localhost:8501
```

---

## 🧪 Model Training

To train the model:

```
python train.py
```

* Dataset configured via `data.yaml`
* YOLOv8 used for training
* Best weights saved in:

```
runs/detect/train/weights/best.pt
```

---

## 📊 Output Example

* Detects helmet ✅
* Detects no helmet ❌
* Draws bounding boxes

(Add screenshots here for better presentation)

---

## ⚠️ Note

* Dataset and trained model weights are not included due to size limitations.
* They can be provided separately if required.

---

## 🔮 Future Improvements

* Real-time video detection (CCTV integration)
* Number plate recognition integration
* Deploy on cloud (AWS / GCP)
* Mobile app integration

---

## ⭐ Support

If you found this project useful, please ⭐ the repository.

