import pyautogui
import numpy as np
import cv2
import time

def takescreenshot():
    time.sleep(3.5)
    image=pyautogui.screenshot()
    w,h=image.size
    print(w,h)
    left = 400
    top = 820
    right = 1500
    bottom = 1020
    
    image = image.crop((left, top, right, bottom))
    image=cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)

    cv2.imwrite(r'C:\Users\Aryan\Desktop\projects\typeracer\1.png',image)