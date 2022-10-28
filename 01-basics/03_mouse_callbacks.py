import cv2

def get_position(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(f'x={x} y={y}')

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(
            img=img,
            center=(x, y),
            radius=50,
            color=(0, 255, 0),
            thickness=2
        )
        cv2.imshow('image', img)


img = cv2.imread(r"assets\tesla.jpg")

#cv2.namedWindow('Damage')
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
cv2.imshow('image', img)
cv2.waitKey(0)



cv2.destroyAllWindows()
