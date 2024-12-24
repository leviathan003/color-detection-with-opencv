import cv2
from utils import get_limits
from PIL import Image

cam_feed = cv2.VideoCapture(0)
yellow = [0,255,255]

while True:
    ret, frame = cam_feed.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_limit, upper_limit = get_limits(color=yellow)
    mask = cv2.inRange(hsv_frame, lower_limit, upper_limit)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (165,0,89), 2)

    cv2.imshow("Cam Feed", frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

cam_feed.release()
cv2.destroyAllWindows()
