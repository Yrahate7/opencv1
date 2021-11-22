import cv2 as cv
import numpy as np

# Create a blank image of resolution 500x500 with 3 color channels and whoose every data bit is an unsigned int of 8 bits
blank = np.zeros((500,500,3),dtype="uint8")

cv.imshow("blank",blank)

blank[:] = 0,255,0

cv.imshow("green",blank)


cv.waitKey(0)