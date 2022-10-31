import cv2

oryginal_img = cv2.imread(r'assets\poland.png')
img = oryginal_img.copy()
#cv2.imshow('original_img', img)
img = cv2.copyMakeBorder(
    src=img,
    top=20,
    bottom=20,
    left=20,
    right=20,
    borderType=cv2.BORDER_CONSTANT,
    value=(255, 255, 255)
)
grey = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
#cv2.imshow('grey', grey)

thresh = cv2.threshold(src=grey, thresh=250, maxval=255, type=cv2.THRESH_BINARY)[1]
cv2.imshow('thresh', thresh)

contours = cv2.findContours(image=thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)[0]
print(f'[INFO] Liczba wszystkich konturów: {len(contours)}')

img_cnt = cv2.drawContours(image=img, contours=[contours[0]], contourIdx=-1, color=(0, 255, 0), thickness=2)
img_cnt = cv2.drawContours(image=img, contours=[contours[1]], contourIdx=-1, color=(0, 255, 0), thickness=2)
cv2.imshow('contours', img_cnt)

countour = contours[0]
leftmost = countour[countour[:, :, 0].argmin()][0]
rightmost = countour[countour[:, :, 0].argmax()][0]
topmost = countour[countour[:, :, 1].argmin()][0]
bottommost = countour[countour[:, :, 1].argmax()][0]

for point in [leftmost, rightmost, topmost, bottommost]:
    cv2.circle(img, center=tuple(point), radius=10, color=(0, 0, 255), thickness=1)
cv2.imshow('img', img)
cv2.waitKey(0)
