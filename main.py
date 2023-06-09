import cv2
from imutils.video import VideoStream


video = VideoStream(src=0).start()

while True:
    frame = video.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow("Intrusion Warning", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
video.stop()
cv2.destroyAllWindows()