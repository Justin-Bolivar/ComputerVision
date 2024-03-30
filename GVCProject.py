import cv2
import numpy as np

img = cv2.imread('Images\Image.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

mask = cv2.inRange(hsv, lower_red, upper_red)

lower_purple = np.array([130, 100, 100])
upper_purple = np.array([179, 255, 255])

hsv[mask > 0] = [130, 255, 255]
purple_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

cv2.imshow('Purple Image', purple_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
