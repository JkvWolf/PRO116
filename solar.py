import cv2

img = cv2.imread('solar-system.jpg')



cv2.putText(
    img,
    'Sun',
    (20, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    'Mercury',
    (125, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    'Venus',
    (225, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    'Earth',
    (325, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    'Moon',
    (350, 175),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    'Mars',
    (420, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    'Jupiter',
    (600, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    'Saturn',
    (775, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

cv2.putText(
    img,
    'Uranus',
    (975, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (0,0,0)
)

cv2.putText(
    img,
    'Neptune',
    (1150, 200),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)


cv2.imshow('output',img)

cv2.imwrite('Solar_systemwithname.jpg',img)

cv2.waitKey(0)