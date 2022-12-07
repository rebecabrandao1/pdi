#%%
import numpy as np
import cv2 as cv
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt

 #%%

img = cv.imread('sophiaeosmeninos/CERTA.jpg', cv.IMREAD_GRAYSCALE)
_, thresh = cv.threshold(img, 120, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
plt.imshow(thresh, cmap = 'gray')
#%%
#window_name = 'Beontag'

x1 = 0 #0
y1 = 400 #850
x2 = 1200 #2000 #1080
y2 = 750 #1300
img =  cv.rotate(thresh, cv.ROTATE_90_COUNTERCLOCKWISE)


frame = img[y1:y2, x1:x2]
out = frame.copy()
plt.imshow(out, cmap = 'gray')
#%%
#kernel = np.ones((3, 3), np.uint8)
#thresh = cv.dilate(out, kernel, iterations=1)
contours, _ = cv.findContours(out, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

#%%
bboxes = []
for cnt in contours:
  area = cv.contourArea(cnt)
  xmin, ymin, width, height = cv.boundingRect(cnt)
  extent = area / (width * height)
  #print('entra aqui')
  if (extent > np.pi / 4) and (area > 100):
    bboxes.append((xmin, ymin, xmin + width, ymin + height))#%%
qrs = []
info = set()
for xmin, ymin, xmax, ymax in bboxes:
  roi = out[ymin:ymax, xmin:xmax]
  detections = decode(roi)
  for barcode in detections:
     info.add(barcode.data.decode('utf-8'))
     # bounding box coordinates
     x, y, w, h = barcode.rect
     qrs.append((xmin + x, ymin + y, xmin + x + w, ymin + y + height))
#print('informações do qr')
print(info)

