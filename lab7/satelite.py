import math

import numpy as np
import cv2
import matplotlib.pyplot as plt

#Importa e converta para RGB
img = cv2.imread('Satelite.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



#Convertendo para preto e branco (RGB -> Gray Scale -> BW)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
a = img_gray.max()
_, thresh = cv2.threshold(img_gray, a/2*1.7, a,cv2.THRESH_BINARY_INV) #alterar aqui


tamanhoKernel = 5                                                     #alterar aqui
kernel = np.ones((tamanhoKernel,tamanhoKernel), np.uint8)
thresh_open = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

#Filtro de ruído (bluring)
img_blur = cv2.blur(img_gray, ksize=(tamanhoKernel,tamanhoKernel))

img_open = cv2.morphologyEx(img_blur, cv2.MORPH_OPEN, kernel)

img_close = cv2.morphologyEx(img_open, cv2.MORPH_CLOSE, kernel)

# Detecção borda com Canny (sem blurry)
edges_gray = cv2.Canny(image=img_gray, threshold1=a/1, threshold2=a/1.4) #alterar aqui
# Detecção borda com Canny (com blurry)
edges_blur = cv2.Canny(image=img_close, threshold1=a/1.5, threshold2=a/2) #alterar aqui



# contorno - pega o maior contorno, o codigo anterior, pelo q entendi, pegava todos os contornos
contours, _ = cv2.findContours(edges_blur, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)

img_copy = img.copy()
if contours:
    final = cv2.drawContours(img_copy, [contours[0]], -1, (255, 0, 0), 2)
else:
    final = img_copy.copy()


#plot imagens
imagens = [img,img_blur,img_gray,edges_gray,edges_blur,thresh,thresh_open,final]
formatoX = math.ceil(len(imagens)**.5)
if (formatoX**2-len(imagens))>formatoX:
    formatoY = formatoX-1
else:
    formatoY = formatoX

plt.figure(figsize=(13, 13))

for i in range(len(imagens)):
    plt.subplot(formatoY, formatoX, i + 1)
    plt.imshow(imagens[i],'gray')
    plt.xticks([]),plt.yticks([])
plt.show()