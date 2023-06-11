# Importing Modules
import cv2
import os

#Importing OpenCV's haarcascade trained data
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Getting Image Directory
dir = os.getcwd() + "<yourimgname.yourimgext>" 

#Feeding the image to openCV
img = cv2.imread(dir)
grayscale_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Converting the Image to Grayscale

#Getting the Coordinates of the Image to create Rectangle
face_coordinates = trained_face_data.detectMultiScale(grayscale_img) #Gives a list containing x,y coordinates of top_left point and box size

#Drawing rectangle for every face found by a loop
for (x,y,w,h) in face_coordinates:     
    cv2.rectangle(img,(x,y) ,  (x+w,y+h), (0,255,0) , 1)


#Showing the final Image
cv2.imshow("ML_Face_Detector" , img)
# print(face_coordinates)
cv2.waitKey() #-->To keep the window open
print("code complete with 0 error")#for debugging
