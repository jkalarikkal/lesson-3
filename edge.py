import cv2

img = cv2.imread("pika1.png")
cv2.imshow("Og image", img)

t_lower = 1200
t_upper = 1400

edge= cv2.Canny(img, t_lower, t_upper)
cv2.imshow("edge image", edge)

cv2.waitKey(0)
cv2.destroyAllWindows()