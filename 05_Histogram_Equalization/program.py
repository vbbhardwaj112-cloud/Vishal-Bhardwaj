import cv2
import numpy as np
img = cv2.imread("input2.jpg",0)
equalized = cv2.equalizeHist(img)
cv2.imshow("output.png",img)
cv2.imshow("equalized",equalized)
cv2.imwrite("output.png",equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()