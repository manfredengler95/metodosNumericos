import cv2

import numpy as np

from matplotlib import pyplot as plt


def hola():
    # OpenCV program to perform Edge detection in real time
    # import libraries of python OpenCV
    # where its functionality resides
    import cv2

    # np is an alias pointing to numpy library
    import numpy as np

    # capture frames from a camera
    cap = cv2.VideoCapture(0)

    # loop runs if capturing has been initialized
    while (1):

        # reads frames from a camera
        ret, frame = cap.read()

        # converting BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)#Se obtiene un histograma basada en las saturaciones de colores.



        # define range of red color in HSV
        lower_red = np.array([30, 150, 50])
        upper_red = np.array([255, 255, 180])

        blue_lower = np.array([80, 150, 100], np.uint8)
        blue_upper = np.array([150, 255, 255], np.uint8)
        blue = cv2.inRange(hsv, blue_lower, blue_upper)  # Se crea una mascara utilizando intervalos de color azul.

        # create a red HSV colour boundary and
        # threshold HSV image
        mask = cv2.inRange(hsv, lower_red, upper_red) # Se crea una mascara utilizando intervalos de color rojo.

        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame, frame, mask=mask)



        # Display an original image
        cv2.imshow('Original', frame)

        # finds edges in the input image image and
        # marks them in the output map edges
        edges = cv2.Canny(frame, 100, 200)

        # Display edges in a frame
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)
        cv2.imshow('Edges', edges)


        # Wait for Esc key to stop
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    # Close the window
    cap.release()

    # De-allocate any associated memory usage
    cv2.destroyAllWindows()
