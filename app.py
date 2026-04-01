import streamlit as st
from ultralytics import YOLO
import numpy as np
from PIL import Image

# Title
st.title("Helmet Detection App ")

# Load model (cached to avoid reloading on every run)
@st.cache_resource
def load_model():
    return YOLO("runs/detect/train12/weights/best.pt")

model = load_model()

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    img = np.array(image)
    results = model(img)

    result_img = results[0].plot()
    st.image(result_img, caption="Detected Image", use_container_width=True)
 
    # Show labels and confidence scores
    boxes = results[0].boxes
    if boxes is not None and len(boxes) > 0:
        st.write("### Detection Results:")
        for box in boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            label = "Helmet" if cls == 0 else "No Helmet"
            st.write(f"{label} ({conf:.2f})")
    else:
        st.warning("No object detected")