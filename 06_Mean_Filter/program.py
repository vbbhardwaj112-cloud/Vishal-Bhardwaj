import cv2
import numpy as np
img = cv2.imread("input3.jpg",0)
mean = cv2.blur(img,(5,5))
cv2.imshow("output.png",img)
cv2.imshow("mean image",mean)
cv2.imwrite("output.png",mean)
cv2.waitKey(0)
cv2.destroyAllWindows()