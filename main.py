import cv2 as cv

# reads path to an image and returns image as a matrix of pixels
img = cv.imread('Photos/cat.jpg')


# Shows image in a window with the first parameter as name and using matrix of pixels (as Second parameter)
cv.imshow('cat',img)

# waits for key to be pressed, and with the given delay as parameter, it closes the image opened in a window
cv.waitKey(0)


# Reading video

# Integer passed as an argument to the video capture method means the device id of the camera connected to your system
# capture = cv.VideoCapture(0)


def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)



# Video path passed as an argument
capture = cv.VideoCapture('Videos/Untitled.mp4')

while True:
    isTrue,frame = capture.read();
    frame_resized = rescaleFrame(frame)
    cv.imshow('video',frame_resized)

    if cv.waitKey(20) & 0xff == ord('d'):
        break;


capture.release()

cv.destroyAllWindows()



