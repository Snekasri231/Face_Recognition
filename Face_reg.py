import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
while(1): 
    _,frame = cam.read()
    grayscale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(grayscale,1.3,4)
    for(x,y,w,h)in face:
        cv2.rectangle(frame,x,y,(x+w,y+h),(0,255,0),2)
    cv2.imshow("face detection",face)
    key = cv2.waitKey(20)
    if key == 1:
       break
cam.release()
cv2.destroyAllWindows()

