import cv2                                            # import libraries of python OpenCV
import winsound
title = 'car control'
cv2.namedWindow(title)                                # capture frames from a camera
video = cv2.VideoCapture(0)
frequency = 2500                                      # Set Frequency To 2500 Hertz
duration = 60                                         # Set Duration To 1000 ms == 1 second

if video.isOpened():                                  # check if video is opened
    rval, frame = video.read()                        # return the value as  video frame
else:
    rval = False                                      # else return 0

# Paths to haarcascade_frontalface_alt.xml and haarcascade_eye.xml files which are available in OpenCV list
faceCascade = cv2.CascadeClassifier("C:/Users/HP/Anaconda2/pkgs/opencv3-3.1.0-py35_0/Library/etc/haarcascades/haarcascade_frontalface_alt.xml") 
eye_cascade = cv2.CascadeClassifier('C:/Users/HP/Anaconda2/pkgs/opencv3-3.1.0-py35_0/Library/etc/haarcascades/haarcascade_eye_tree_eyeglasses.xml')
smile_cascade = cv2.CascadeClassifier('C:/Users/HP/Anaconda2/pkgs/opencv3-3.1.0-py35_0/Library/etc/haarcascades/haarcascade_smile.xml')
font = cv2.FONT_HERSHEY_SIMPLEX
  
# Line thickness of 2 px 
thickness = 2
while rval:                                           # infinite loop till the return value is true
    cv2.imshow(title, frame)                          # Display an image and title in a window 
    rval, frame = video.read()                        # reads frames from a camera

    if len(faceCascade.detectMultiScale(frame))>0:    # check the length of frame in detection               
        faces = faceCascade.detectMultiScale(frame)   # Detects faces of different sizes in the input image

        for (x, y, w, h) in faces:                    # To draw a rectangle in a face(x and y coordinate, width and height)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if w > 0:                                 # if width is greater than 0
                #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)   # draw a reactangle
                
                if len(eye_cascade.detectMultiScale(frame))>0:        # check the lenth of eye frame
                    eyes = eye_cascade.detectMultiScale(frame)        # Detects eyes of different sizes in the input image 
                    for (ex, ey, ew, eh) in eyes:                     # To draw a rectangle in eyes
                        if ew > 0:                                    # if the eye width is greater then 0
                            cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                    smile = smile_cascade.detectMultiScale(frame,scaleFactor=1.8, minNeighbors=20,minSize=(25, 25),)
                    for (ex, ey, ew, eh) in smile:
                        if ew > 0:
                            cv2.rectangle(frame, (ex,ey), (ex+ew, ey+eh), (0,255,255), 2)
                            
                    
    key = cv2.waitKey(1)                                   
    if key == 27: 
        break

video.release()                                                 
cv2.destroyWindow(title)                                               # De-allocate any associated memory usage 
