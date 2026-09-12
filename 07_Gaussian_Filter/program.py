import cv2
import numpy as np
img = cv2.imread("input2.jpg",0)
gaussian = cv2.GaussianBlur(img,(9,9),0)
cv2.imshow("output.png",img)
cv2.imshow("GaussianBlur",gaussian)
cv2.imwrite("output.png",gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()