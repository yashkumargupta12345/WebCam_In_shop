import cv2
import time
from email_sending import send_email

# Capturing The video By the Method - VideoRecorder .
video = cv2.VideoCapture(0)
time.sleep(1)
status_list = []
status = 0
first_frame = None
while True:
    # Extract The Frames From The Video by the read method.
    check, frame = video.read()

    # Converting The Frame To Gray Frame.
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Converting The Gray Frame To Gaussian Frame.
    gaussian_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gaussian_frame

    # Extracting The Objects From The Video Which are Different From The First Frame.
    delta_frame = cv2.absdiff(first_frame, gaussian_frame)
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # Running the Camera
    cv2.imshow("My Video", dil_frame)

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:

        # if Contour Area is less than 2000 that will be an imaginary object.
        if cv2.contourArea(contour) < 2000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)
        if rectangle.any():
            status = 1
    status_list.append(status)
    status_list = status_list[-2:]

    # Sending the e-mail to the owner as the customer exits the frame.
    if status_list[0] == 1 and status_list[1] == 0:
        send_email()

    print(status_list)
    cv2.imshow('My Video', frame)
    key = cv2.waitKey(1)

    # exit the webcam as the owner presses the 'q' command.
    if key == ord("q"):
        break

video.release()




a=[2,1,3,5,2,4]
a.remove(2)
print(a)


m = [[x, x + 1, x + 2] for x in range(0, 3)]

print(m)