import cv2

img = cv2.imread("pika1.png")
cv2.imshow("Og Image", img)

rimage1 = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
rimage2 = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
rimage3 = cv2.rotate(img,cv2.ROTATE_180)

cv2.imshow("Clockwise", rimage1)
cv2.imshow("Anticlockwise", rimage2)
cv2.imshow("UPSIDE DOWN", rimage3)

cv2.waitKey(0)
cv2.destroyAllWindows()
