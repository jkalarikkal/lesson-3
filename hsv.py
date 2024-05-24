import cv2

img = cv2.imread("pika1.png")
cv2.imshow("og image", img)

hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
cv2.imshow("Hsv image", hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()