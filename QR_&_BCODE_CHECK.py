import cv2
import numpy as np
from pyzbar.pyzbar import decode #For read barcode and Qr

o=cv2.VideoCapture(1) #For open camera

with open("Availability_check.txt") as f:
    Y=f.read().splitlines() #That text file which has indian name

while True:
    success, i = o.read()
    for b in decode(i):
        m=b.data.decode('utf-8')
        print(m) #Print that data which is inside the QR or Barcode

        if m in Y:
            con="INDIAN"
            conCo=(0,255,255)
        else:
            con="NOT-INDIAN"
            conCo=(102,102,255)

        p=np.array([b.polygon],np.int32)
        p=p.reshape((-1,1,2))
        cv2.polylines(i,[p],True,conCo,3)

        p2=b.rect
        cv2.putText(i,con,(p2[0],p2[1]),cv2.FONT_HERSHEY_PLAIN,2.5,conCo,2)

    if cv2.waitKey(1) == ord('e'): #To stop our program
        break
    cv2.imshow("Image", i)
