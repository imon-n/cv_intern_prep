import cv2

image = cv2.imread("football.png")
# print(image)

imageres=cv2.resize(image,(640,480))
print(image)

gray = cv2.cvtColor(imageres,cv2.COLOR_BGR2GRAY)
# print(gray)

blur = cv2.GaussianBlur(gray,(5,5),0)
edges = cv2.Canny(blur, 50, 150)
print(edges)

cv2.imwrite("output.edges.jpg",edges)

cv2.imshow("orgial",image)
cv2.imshow("reshape",imageres)
cv2.imshow("gray",gray)
cv2.imshow("edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()