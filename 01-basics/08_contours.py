import cv2

oryginal_img = cv2.imread(r'assets\python.png')
img = oryginal_img.copy()
cv2.imshow('original_img', img)

# konwersja do skali szarości

gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

# wydobycie maski

thresh = cv2.threshold(src=gray, thresh=250, maxval=255, type=cv2.THRESH_BINARY)[1]
cv2.imshow('thresh', thresh)

# detekcja konturów

# canny = cv2.Canny(image=thresh, threshold1=250, threshold2=50)
# cv2.imshow('canny', canny)

contours = cv2.findContours(image=thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)[0]
print(f'[INFO] Liczba wszystkich konturów: {len(contours)}')


img_cnt = cv2.drawContours(image=img.copy(), contours=[contours[1]], contourIdx=-1, color=(0, 255, 0), thickness=2)
cv2.imshow('contour', img_cnt)




# pole konturów

max_area = 0
idx_area = 0
for idx, contour in enumerate(contours):
    area = cv2.contourArea(contour=contour, oriented=True)
    if area > max_area:
        max_area = area
        idx_area = idx


img_cnt = cv2.drawContours(image=img.copy(), contours=[contours[idx_area]], contourIdx=-1, color=(0, 255, 255), thickness=2)
cv2.imshow('contour', img_cnt)

perimeter = cv2.arcLength(curve=contours[idx_area], closed=True)
print(f'Długość konturu: {perimeter}')
cv2.waitKey(0)