import cv2
import numpy as np
img = cv2.imread("input4.jpg",0)
median = cv2.medianBlur(img,15)
cv2.imshow("output.png",img)
cv2.imshow("medianBlur",median)
cv2.imwrite("output.png",median)
cv2.waitKey(0)
cv2.destroyAllWindows()