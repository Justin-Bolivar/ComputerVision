from huggingface_hub import hf_hub_download
from ultralytics import YOLO
from supervision import Detections
from PIL import Image, ImageDraw
import numpy as np

# download model
model_path = hf_hub_download(repo_id="arnabdhar/YOLOv8-Face-Detection", filename="model.pt")

# load model
model = YOLO(model_path)

# inference
image_path = "Images/portrait.JPG"
image = Image.open(image_path)
output = model(image)
results = Detections.from_ultralytics(output[0])

# Draw bounding boxes on the image
draw = ImageDraw.Draw(image)
for detection in results.xyxy:
    # Extract bounding box coordinates
    x1, y1, x2, y2 = detection
    # Draw bounding box rectangle
    draw.rectangle([x1, y1, x2, y2], outline="red", width=2)

# Show image with bounding boxes
image.show()
