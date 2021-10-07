# pip3 install opencv-python
import cv2
import numpy as np
# pip install pyautogui
import pyautogui

srcSize = (1920, 1080) # Screen size of video
vwr = cv2.VideoWriter_fourcc(*'XVID') 
output = cv2.VideoWriter("video1.avi", vwr, 20, (srcSize))   # Setting video variabloe

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output.write(frame)


# testing 