import cv2
from cv2 import imread
img=cv2.imread("solar-system.jpg")
cv2.imshow("output",img)
cv2.waitKey(0)

cv2.putText(img,"sun",
(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(225,225,225)

)
cv2.putText(img,"mercury",
(20,400),cv2.FONT_HERSHEY_COMPLEX,0.5,(205,205,225)

)
