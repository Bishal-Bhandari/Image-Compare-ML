import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('33505.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('33505 - Copy.jpg', cv2.IMREAD_GRAYSCALE)

diff_cod = cv2.subtract(img1, img2)

imS = cv2.resize(img1, (960, 540))
cv2.imshow('image',imS)
cv2.waitKey(0)
cv2.destroyAllWindows()