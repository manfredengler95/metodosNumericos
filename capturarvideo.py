import numpy as np
import cv2

def mostrar():
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # hsv hue sat value
        lower_red = np.array([150, 150, 50])
        upper_red = np.array([255, 255, 255])

        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(frame, frame, mask = mask)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

        # Display the resulting frame
        #cv2.imshow('frame', gray)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    # When everything done, release the capture

    cv2.destroyAllWindows()
    cap.release()
