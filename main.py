import cv2
import numpy as np

# Set up video capture
cap = cv2.VideoCapture(0)

# Define range of colors to detect (blue in this case)
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])

# ...

# Code utilizing OpenCV functions
while True:
    # Read frame from video capture
    ret, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the resulting frame
    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', res)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ...