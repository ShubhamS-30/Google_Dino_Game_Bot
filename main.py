import pyautogui
from PIL import Image, ImageGrab
import time
import adjustment


#                                          CHROME DINO GAME BOT
#   GAME LINK - chrome://dino/

# THIS FUNCTION CHECKS IF IT IS DAY OR NIGHT IN THE GAME
# 255 MEANS WHITE AND 0 BLACK
def background(data, X1, X2, Y1, Y2):
    for i in range(X1, X2):
        for j in range(Y1, Y2):
            if data[i, j] == 255:
                return 'day'
    return 'night'

# DURING NIGHT OBSTACLES ARE IN WHITE COLOUR
# NESTED LOOP CHECKS FOR WHITE PIXELS


def CollisionNight(data, X1, X2, Y1, Y2):
    for i in range(X1, X2):
        for j in range(Y1, Y2):
            if data[i, j] > 100:
                return True
    return False

# DURING DAY OBSTACLES ARE IN GREY/BLACK COLOUR
# NESTED LOOP CHECKS FOR GREY/BLACK PIXELS


def CollisionDay(data, X1, X2, Y1, Y2):
    for i in range(X1, X2):
        for j in range(Y1, Y2):
            if data[i, j] < 100:
                return True
    return False


# EXPORTING VALUES FROM ADJUSTMENT.PY
X1 = adjustment.X1
X2 = adjustment.X2
Y1 = adjustment.Y1
Y2 = adjustment.Y2
XB1 = adjustment.XB1
XB2 = adjustment.XB2
YB1 = adjustment.YB1
YB2 = adjustment.YB2
if __name__ == '__main__':

    # EXECUTION CODE

    print('Game Starting !!')
    # AGENT STARTS 2 SEC AFTER EXECUTION OF PROGRAM
    # DURING THESE 2 SECONDS OPEN THE CHROME TAB WITH DINO GAME AND PRESS SPACEBAR KEY ONCE
    time.sleep(2)
    while True:
        image = ImageGrab.grab().convert('L')
        # TAKES SCREENSHOT AND CONVERTS IT TO BLACK AND WHITE IMAGE

        data = image.load()
        # CONVERTS THE SCREENSHOT INTO AN ARRAY THAT CONTAINS PIXEL INFORMATION

        if background(data, XB1, XB2, YB1, YB2) == 'night':
            if CollisionNight(data, X1, X2, Y1, Y2):
                pyautogui.keyDown('up')
                # IF A WHITE PIXEL IS DETECTED ABOVE COMMAND IS USED TO PRESS UP KEY TO MAKE DINO JUMP
        else:
            if CollisionDay(data, X1, X2, Y1, Y2):
                pyautogui.keyDown('up')
                # IF A BLACK PIXEL IS DETECTED ABOVE COMMAND IS USED TO PRESS UP KEY TO MAKE DINO JUMP
