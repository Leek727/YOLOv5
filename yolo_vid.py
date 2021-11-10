import torch
import cv2
import numpy as np

cap = cv2.VideoCapture("ped.webm")
# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

while 1:  # 727
    # Take each frame
    _, frame = cap.read()
    
    results = model(frame)
    results.save()
    #results.
  
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()


