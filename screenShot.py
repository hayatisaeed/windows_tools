import pyautogui
import cv2
import numpy as np
from tkinter import *
from time import sleep
from time import time, ctime
from getpass import getuser
import os
import GUI

root = Tk()
root.title('ScreenShot v.1')
root.geometry("250x80")

def shot():
    root.wm_state('iconic')
    filename = ent.get()
    sleep(1)
    img = pyautogui.screenshot()
    t = ctime(time()).replace(':','')
    user = getuser()
    pathh = os.path.dirname(__file__)
    try:
        img.save('%s\%s.png'%(pathh, filename))
    except:
        img.save("%s\ScreenShot %s.png"%(pathh,t))
# show the gui again
GUI.show_me()
        
lbl = Label(text="Enter File name :").pack()
ent = Entry()
ent.pack()
btn = Button(text="take", command=shot)
btn.pack()

root.mainloop()
