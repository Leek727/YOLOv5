import torch

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Images
imgs = ['https://ultralytics.com/images/zidane.jpg']  # batch of images

# Inference
results = model(imgs)

# Results
results.print()
results.show()

#print(results.xyxy[0])  # img1 predictions (tensor)
#print(results.pandas().xyxy[0])  # img1 predictions (pandas)