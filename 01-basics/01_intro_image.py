import cv2

print(cv2.__version__)

image = cv2.imread(r"C:\Users\Rafal\PycharmProjects\ocvProjekty\01-basics\assets\bear.jpg")

cv2.imshow(winname="image", mat=image)
cv2.waitKey(delay=5000)
