import cv2
import numpy as np
import matplotlib.pyplot as plt

original_image = cv2.imread('Images/Image2.jpg')

gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(original_image, 100, 200)

histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

fig, axs = plt.subplots(2, 2)

axs[0, 0].imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
axs[0, 0].set_title('Original Image')

axs[0, 1].imshow(edges, cmap='gray')
axs[0, 1].set_title('Edges')

axs[1, 0].imshow(gray_image, cmap='gray')
axs[1, 0].set_title('Grayscale Image')

axs[1, 1].plot(histogram)
axs[1, 1].set_title('Histogram')

print('Filename:', 'Images/Image2.jpg')
print('Format:', 'RGB')
print('Width:', original_image.shape[1])
print('Height:', original_image.shape[0])
print('Size:', original_image.size)

pixel_value = original_image[1060, 1240]
print('Pixel value at (100, 100):', pixel_value)

plt.show()