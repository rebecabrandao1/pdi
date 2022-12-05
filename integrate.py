#%%
import numpy as np
import cv2 as cv
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt
#%%
def verificaqr(image):


   scale = 0.3
   width = int(image.shape[1] * scale)
   height = int(image.shape[0] * scale)
   image = cv.resize(image, (width, height))
#achando um limiar
   gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
   _, thresh = cv.threshold(gray, 120, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
#%%
# The bigger the kernel, the more the white region increases.
# If the resizing step was ignored, then the kernel will have to be bigger
# than the one given here.
   kernel = np.ones((3, 3), np.uint8)
   thresh = cv.dilate(thresh, kernel, iterations=1)
   contours, _ = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#%%
   bboxes = []
   for cnt in contours:
      area = cv.contourArea(cnt)
      xmin, ymin, width, height = cv.boundingRect(cnt)
      extent = area / (width * height)
  
  # filter non-rectangular objects and small objects
      if (extent > np.pi / 4) and (area > 100):
       bboxes.append((xmin, ymin, xmin + width, ymin + height))#%%
qrs = []
info = set()
for xmin, ymin, xmax, ymax in bboxes:
  roi = image[ymin:ymax, xmin:xmax]
  detections = pyzbar.decode(roi, symbols=[pyzbar.ZBarSymbol.QRCODE])
  for barcode in detections:
     info.add(barcode.data)
     # bounding box coordinates
     x, y, w, h = barcode.rect
     qrs.append((xmin + x, ymin + y, xmin + x + w, ymin + y + height))
#%%

img = cv.imread('sophiaeosmeninos/CERTA.jpg', cv.IMREAD_GRAYSCALE)
plt.imshow(img, cmap = 'gray')
#%%
#window_name = 'Beontag'

x1 = 0 #0
y1 = 400 #850
x2 = 1200 #2000 #1080
y2 = 750 #1300
img =  cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)

frame = img[y1:y2, x1:x2]
out = frame.copy()
plt.imshow(out, cmap = 'gray')

#%%
print('entra aqui')
for d in pyzbar.decode(out):
    print('entrou')
    s = d.data.decode()#qr code reader result --> comparar no comparador do roger
    print(s) #compare with seriesnumber
    print('devia estar aqui')
    out= cv.rectangle(out, (d.rect.left, d.rect.top),
                                (d.rect.left + d.rect.width, d.rect.top + d.rect.height), (0, 255, 0), 3)
    out = cv.putText(out, s, (d.rect.left, d.rect.top + d.rect.height),
                            cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv.LINE_AA)
#cv.imshow(window_name, frame)
# Display the resulting frame
#%%

#plt.imshow(out)




# %%
