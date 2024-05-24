import cv2

img = cv2.imread("pika1.png")
cv2.imshow('Og image', img)

greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey image", greyscale)

cv2.waitKey(0)
cv2.destroyAllWindows()