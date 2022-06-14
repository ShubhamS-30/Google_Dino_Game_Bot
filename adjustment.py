import pyautogui
from PIL import Image, ImageGrab
import time


# MAKE CHANGES HERE
X1 = 220
X2 = 510
Y1 = 660
Y2 = 661
XB1 = 150
XB2 = 151
YB1 = 250
YB2 = 251

# TO MAKE ADJUSTMENTS CHANGE THE LOOPS RANGE BY CHANGING VALUES OF X1,X2,Y1,Y2 AND XB1,XB2,YB1,YB2 FOR BACKGROUND

time.sleep(2)
image = ImageGrab.grab().convert('L')
data = image.load()
print(data)
# THIS LOOP CHECKS THE BACKGROUND
for i in range(XB1, XB2):
    for j in range(YB1, YB2):
        data[i, j] = 255
# THIS LOOP CHECKS FOR COLLISION
for i in range(X1, X2):
    for j in range(Y1, Y2):
        data[i, j] = 255
# SHOWS THE SCREENSHOT
# image.show()
