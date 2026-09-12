import cv2
import numpy as np
img = cv2.imread("input2.jpg",0)
dft = cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
print("original shape",img.shape)
print("DFT shape",dft.shape)
print("Shfted dft shape",dft_shift.shape)
magnitude = cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1])
magnitude = cv2.normalize(magnitude,None,0,255,cv2.NORM_MINMAX)
magnitude = np.uint8(magnitude)
cv2.imwrite("output.png",magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()