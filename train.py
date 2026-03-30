from ultralytics import YOLO
model = YOLO("yolov8n.pt")
model.train(
    data="C:/object_detection_project/dataset/data.yaml",
    epochs=10,
    imgsz=640
)
print("Training Done")