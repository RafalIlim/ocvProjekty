import cv2

img = cv2.imread(r'assets\grey.png')
print(img)
cv2.imshow('img', img)

# ----------------
# ------Tresh_binary
# ----------------

# thressh_binary = cv2.threshold(src=img, thresh=150, maxval=255, type=cv2.THRESH_BINARY)[1]
#
# cv2.imshow('thresh_binary', thressh_binary)

for thresh in [0, 50, 100, 150, 200]:
    thressh_binary = cv2.threshold(src=img, thresh=thresh, maxval=255, type=cv2.THRESH_BINARY)[1]
    cv2.imshow(f'thressh_binary: {thresh}', thressh_binary)
    cv2.waitKey(1000)
    cv2.destroyWindow(f'thressh_binary: {thresh}')


cv2.waitKey(0)
