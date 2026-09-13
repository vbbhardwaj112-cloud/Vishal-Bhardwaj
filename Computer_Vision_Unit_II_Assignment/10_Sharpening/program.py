import cv2
import numpy as np
img = cv2.imread("input1.jpg",0)
kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
sharp = cv2.filter2D(img,-1,kernel)
cv2.imshow("output.png",img)
cv2.imshow("Sharpend image",sharp)
cv2.imwrite("output.png",sharp)
cv2.waitKey(0)
cv2.destroyAllWindow()