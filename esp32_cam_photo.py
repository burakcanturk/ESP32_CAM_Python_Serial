from esp32_cam import esp32cam
import cv2

cam = esp32cam(port = "COM9")

while True:

    frame = cam.read()

    frame = cv2.resize(frame, (640, 480))

    cv2.imshow("CAM", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
