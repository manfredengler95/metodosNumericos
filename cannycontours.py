import cv2
import numpy as np

cap = cv2.VideoCapture(0)
size = 5
while (1):
    ret, frame = cap.read()
    # Pre-processing: Convert frame to standard size, 1024x768
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 9)
    edges = cv2.Canny(gray, 10, 25)
    _, contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        area = cv2.contourArea(box)
        ratio = area / size
        if ratio < 0.015:
            continue
        # Mark box as segment


def auto_canny(image, sigma=0.5):
    v = np.median(image)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    return cv2.Canny(image, lower, upper)