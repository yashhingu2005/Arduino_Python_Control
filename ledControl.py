import math  # to do calculations
import time  # to display frame rate

import cv2  # Open-CV Library to create the video

import HandTrackingModule as htm  # Handmade module to detect hands and get coordinates

import serial
import time

arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)


def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


# frame details
wCam, hCam = 640, 480
wScr = 1920
frameR = 10  # Frame Reduction
smoothening = 5
hScr = 1080
plocX, plocY = 0, 0
clocX, clocY = 0, 0
#########################

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)  # Selecting camera

cap.set(3, wCam)  # Setting the height and width of view
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)  # creating an object for class handDetector()


# Map function to convert base 640/480 values to 1920/1080
def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


# infinite loop to run the program continuously
while True:
    chr
    success, img1 = cap.read()
    img = cv2.flip(img1, 1)  # Mirroring the frame
    img = detector.findHands(img, draw=False)  # calling the findHands function from the class handDetector()
    lmList = detector.findPosition(img, draw=False)  # lmlist Stores the detected hand landmarks
    cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                  # Drawing a rectangle in the video frame to act as a boundary box
                  (255, 0, 255), 2)
    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]  # getting the X,Y coordinates for the index finger
        x2, y2 = lmList[8][1], lmList[8][2]  # getting the X,Y coordinates for the thumb
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2  # getting the center point between both the fingers
        length = math.hypot(x2 - x1, y2 - y1)  # calculating the distance between the two fingers

        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)  # highlighting the index finger
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)  # Highlighting the thumb

        cv2.circle(img, (cx, cy), 15, (255, 0, 255),
                   cv2.FILLED)  # highlighting the center point between the two fingers

        cv2.line(img, (x1, y1), (x2, y2), thickness=3,
                 color=(255, 0, 255))  # Drawing a line between both the fingers inside the video frame

        # if the user closes their fingers the distance between them decreases so if the distance is less enough
        # the program would simulate a right click
        if length < 40:
            write_read("1")
        else:

            write_read("0")

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)  # printing the frame rate of the entire process

    cv2.imshow("Image", img)  # displaying the video output
    cv2.waitKey(1)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)  # printing the frame rate of the entire process

    cv2.imshow("Image", img)  # displaying the video output
    cv2.waitKey(1)
