import cv2
import numpy as np
def _bounding_box_of(contour):
    rotbox = cv2.minAreaRect(contour)
    coords = cv2.boxPoints(rotbox)

    xrank = np.argsort(coords[:, 0])

    left = coords[xrank[:2], :]
    yrank = np.argsort(left[:, 1])
    left = left[yrank, :]

    right = coords[xrank[2:], :]
    yrank = np.argsort(right[:, 1])
    right = right[yrank, :]

    #            top-left,       top-right,       bottom-right,    bottom-left
    box_coords = tuple(left[0]), tuple(right[0]), tuple(right[1]), tuple(left[1])
    box_dims = rotbox[1]
    box_centroid = int((left[0][0] + right[1][0]) / 2.0), int((left[0][1] + right[1][1]) / 2.0)

    return box_coords, box_dims, box_centroid