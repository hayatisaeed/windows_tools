import pyautogui
import cv2
import numpy as np
from tkinter import *
from time import sleep
from time import time, ctime
from getpass import getuser
import os

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
    # show the window again
    root.deiconify()
    # show 'saved' message
    root.geometry("250x120")
    lbl95 = Label(text="screen shot \"%s.png\" \n saved in \n \"%s\""%(filename, pathh))
    lbl95.pack()
        
lbl = Label(text="Enter File name :").pack()
ent = Entry()
ent.pack()
btn = Button(text="take", command=shot)
btn.pack()

root.mainloop()
