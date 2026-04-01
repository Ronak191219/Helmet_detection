from ultralytics import YOLO
model = YOLO("yolov8n.pt")
model.train(
    data="dataset/data.yaml",   # 👈 relative path use kar
    epochs=5,
    imgsz=640
)
print("Training Done")