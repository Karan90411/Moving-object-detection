import cv2
import time
import imutils
def detection():
    cam = cv2.VideoCapture(0)
    time.sleep(1)

# Initialize Firstframe outside the loop
    Firstframe = None

    while True:
        _, img = cam.read()
        text = "Normal"
        img = imutils.resize(img, width=500)

        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        grayImg = cv2.GaussianBlur(grayImg, (21, 21), 0)

        if Firstframe is None:
            Firstframe = grayImg  # Fix the variable name
            continue

        imgdiff = cv2.absdiff(Firstframe, grayImg)
        thresImg = cv2.threshold(imgdiff, 25, 255, cv2.THRESH_BINARY)[1]
        thresImg = cv2.dilate(thresImg, None, iterations=2)
        cont = cv2.findContours(thresImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cont = imutils.grab_contours(cont)
        for c in cont:
            area = 1200  # You need to define the 'area' variable
            if cv2.contourArea(c) < area:
                continue
            (x, y, w, h) = cv2.boundingRect(c)
            text = "Moving object detected"


        print(text)
        cv2.putText(img, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.imshow("camfeed", img)
        key = cv2.waitKey(2) & 0xFF

        if key == ord("q"):
            break

# Release the camera and close all OpenCV windows
# cam.release()
detection()
cv2.destroyAllWindows()
