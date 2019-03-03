from PIL import ImageGrab
import cv2
import numpy as np


scale = 0.3

while True:
    img = ImageGrab.grab()
    img_array = np.array(img)
    img_array = cv2.resize(img_array, dsize=None, fx=scale, fy=scale)
    img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)

    cv2.imshow("Tutorial", img_array)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()