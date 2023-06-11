# Importing Modules
import cv2


#Importing OpenCV's haarcascade trained data
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Accessing the Webcam
webcam = cv2.VideoCapture(0)
filter =cv2.imread("filter.png")

while True:
    successful_frame_read, frame = webcam.read() #--> Reading the frames

    # Turning each frame grayscale for analysing
    grayscale_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #Identifying the face coordinates
    face_coordinates = trained_face_data.detectMultiScale(grayscale_frame)

    #Drawing the rectangle
    for (x,y,w,h) in face_coordinates:     
        cv2.rectangle(frame,(x,y) ,  (x+w,y+h), (0,255,0) , 2)

    #Showing each frame
    cv2.imshow("ML_Face_Detector" , frame)
    # print(face_coordinates)
    key = cv2.waitKey(1) #--each frame is waited at for 1 milli-second
    #If escape is pressed loop breaks (ascii-value for esc btn)
    if key == 27:
        break
#Clearing potentially unwanted reference
webcam.release()
print("code complete with 0 error")

 




