import cv2
import numpy as np

import matplotlib.pyplot as plt

# Load the original image
original_image = cv2.imread('Images/Image2.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(original_image, 100, 200)

# Calculate the histogram of the grayscale image
histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

# Display all images in one figure
fig, axs = plt.subplots(2, 2)

# Plot the original image
axs[0, 0].imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
axs[0, 0].set_title('Original Image')

# Plot the edges image
axs[0, 1].imshow(edges, cmap='gray')
axs[0, 1].set_title('Edges')

# Plot the grayscale image
axs[1, 0].imshow(gray_image, cmap='gray')
axs[1, 0].set_title('Grayscale Image')

# Plot the histogram
axs[1, 1].plot(histogram)
axs[1, 1].set_title('Histogram')

# Print the properties of the image
print('Filename:', 'path_to_original_image.jpg')
print('Format:', 'RGB')
print('Width:', original_image.shape[1])
print('Height:', original_image.shape[0])
print('Size:', original_image.size)

# Get the value of a pixel in the image
pixel_value = original_image[1060, 1240]
print('Pixel value at (100, 100):', pixel_value)

# Show the figure
plt.show()