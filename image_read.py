import cv2

image = cv2.imread("../assets/logo-py.jpg")
cv2.imshow("Image window",image)
cv2.waitKey(0)
cv2.destroyAllWindows()