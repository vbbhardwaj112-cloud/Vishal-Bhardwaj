import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("input2.jpg",0)
equalized = cv2.equalizeHist(img)
cv2.imshow("Original",img)
cv2.imshow("Equalized",equalized)
cv2.imwrite("output.png",equalized)
plt.hist(img.ravel(), bins=256, range=[0,256], alpha=0.5, label="Before")
plt.hist(equalized.ravel(), bins=256, range=[0,256], alpha=0.5, label="After")
plt.legend()
plt.savefig("histogram_comparison.png")
cv2.waitKey(0)
cv2.destroyAllWindows()