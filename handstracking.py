import cv2
import mediapipe as mp
cap = cv2.VideoCapture(0)
while (cap.isopened()):
    success , img = cap.read()

    cv2.imshow("HAND TRACKING ", img)
    if cv2.waitkey(0)==113:
        break