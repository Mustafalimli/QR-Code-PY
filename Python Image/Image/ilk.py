import cv2
from matplotlib import pyplot as plt

resim = cv2.imread("Image\\images.jpeg",0)
cv2.namedWindow("resim1",cv2.WINDOW_NORMAL)
cv2.imshow("resim1",resim)

cv2.imshow("resim1",resim)

cv2.destroyWindow("resim1")
cv2.imwrite("Resim-Gri.jpeg",resim) 

plt.imshow(resim,cmap="grey")
plt.show()

