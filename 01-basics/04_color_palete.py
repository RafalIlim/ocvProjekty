import cv2 as cv
import numpy as np

def nothing(x):
    pass

img = np.zeros(shape=(300, 500, 3), dtype='uint8')
cv.namedWindow('Paleta')

#utworzenie pasków przewijania

cv.createTrackbar('Red', 'Paleta', 0, 255, nothing)
cv.createTrackbar('Green', 'Paleta', 0, 255, nothing)
cv.createTrackbar('Blue', 'Paleta', 0, 255, nothing)

while True:
    cv.imshow('Paleta', img)

    #pobierz aktualna pozycję
    r = cv.getTrackbarPos('Red', 'Paleta')
    g = cv.getTrackbarPos('Green', 'Paleta')
    b = cv.getTrackbarPos('Blue', 'Paleta')

    img[:] = [b, g, r]
    if cv.waitKey(20) == 27:
        cv.destroyAllWindows()
        break
