#%%
import numpy as np
import cv2 as cv
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt
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
