import cv2
import numpy as np

def canny(image):
	gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
	blur = cv2.GaussianBlur(gray, (5,5), 0)
	canny = cv2.Canny(blur, 50,150)
	return canny

def point_of_interesed(image):
	height = image.shape[0]
	pollygons = np.array([(200, height), (1000, height), (550, 250)])
	mask = np.zeros_like(image)
	cv2.fillConvexPoly(mask, pollygons, 255)
	return mask

img = cv2.imread('test_image.jpg')
lane_image = np.copy(img)
canny = canny(lane_image)
cv2.imshow('de ce te uiti la titlu', point_of_interesed(canny)) 
cv2.waitKey(0)