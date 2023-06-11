# Face_Identifier

## How it works?
It uses cv2 and its library to identify front facing faces to find them in the image.It uses haarcascades provided by the opencv module to identify the target and draw a rectangle around with some confidence.Here `main.py` analyses test images and can identify faces in the images you assign by changing the variable in the file.You can find faces in real time through your webcam using `main_2.0.py`.

## How Harcascades work?
Haarcascade is a file that cascades on the given input file and funnels down on every pixel until a bunch of pixels for what the algorithm thinks to be a face-like structure.This harcascade is a file with trained data that is capable of doing what was mentioned above.The detector uses haar features to differentiate each pixels and find a relation between them to create a template for something that looks like a face.The algorithm is fed both faces and non-faces and then it learns what makes a face and what does not.
