import cv2

cap=cv2.VideoCapture(0)

while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        canny=cv2.Canny(frame,100,100)
        cv2.imshow("camera",canny)
        if cv2.waitKey(1) & 0xFF==ord('v'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows