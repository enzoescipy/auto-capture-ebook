from pynput.mouse import Controller as Controller_mouse
from pynput.keyboard import Controller as Controller_keyboard
from pynput.keyboard import Key
from pynput.keyboard import Listener
from pynput.mouse import Button  
import numpy as np
import cv2 
import time
import pyautogui
import os
import shutil
import pickle
SLEEP_TIME = 0.1

class Macro():

    mouseController = Controller_mouse()
    keyboardController = Controller_keyboard()
    clicking_pos = None  
    captureRect = [0,0,0,0]

    iter_count = 0

    @classmethod
    def mouse_setpos(cls):
        print("clicking position get. press space to pick.")
        def on_pressed(key):
            if key == Key.space:
                return False
        with Listener(on_press=on_pressed) as listener:
            listener.join()
        
        print(cls.mouseController.position)

        cls.clicking_pos = cls.mouseController.position

    @classmethod
    def mouse_click(cls):
        pos_before = cls.mouseController.position
        cls.mouseController.position = cls.clicking_pos 
        cls.mouseController.click(Button.left,1)
        cls.mouseController.position = pos_before
        time.sleep(SLEEP_TIME) 

    @classmethod
    def capture_rect0(cls):
        print("capture rect 0 pos get. press space to pick.")
        def on_pressed(key):
            if key == Key.space:
                return False
        with Listener(on_press=on_pressed) as listener:
            listener.join()
        pos = cls.mouseController.position
        print(pos)
        cls.captureRect[0] =  pos[0]
        cls.captureRect[1] =  pos[1]

    @classmethod
    def capture_rect1(cls):
        print("capture rect 1 pos get. press space to pick.")
        def on_pressed(key):
            if key == Key.space:
                return False
        with Listener(on_press=on_pressed) as listener:
            listener.join()
        pos = cls.mouseController.position
        print(pos)
        cls.captureRect[2] =  pos[0]
        cls.captureRect[3] =  pos[1]
    
    @classmethod
    def capture_execute(cls):
        img = pyautogui.screenshot()#(cls.captureRect_0_pos[0],cls.captureRect_0_pos[1],cls.captureRect_1_pos[0],cls.captureRect_1_pos[1]))
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        cv2.imwrite("result/{}.png".format(cls.iter_count), img)
        cls.iter_count += 1
        time.sleep(SLEEP_TIME)

    @classmethod
    def crop_images(cls):
        read_num = 0
        while True:
            dir = "result/{}.png".format(read_num)
            if os.path.exists(dir) == False:
                break
            img = cv2.imread(dir, cv2.IMREAD_UNCHANGED)
            x = cls.captureRect[0]  
            y = cls.captureRect[1]
            w = cls.captureRect[2] - x
            h = cls.captureRect[3] - y
            img = img[y: y + h, x: x + w]    
            #cv2.namedWindow("img")
            #cv2.imshow("img",img)  
            #cv2.waitKey(0)  
            #cv2.destroyAllWindows()  
            cv2.imwrite(dir, img)  
            read_num += 1


choice = input("0 : capture mod, 1 : crop mod => :")
if choice == "0":

    if os.path.exists("result"):
        shutil.rmtree("result") 
        os.mkdir("result")
    else:
        os.mkdir("result")   

    Macro.capture_rect0()
    Macro.capture_rect1()
    Macro.mouse_setpos()

    page_count = int(input("how many pages in the book?  (int) : "))



    input("Start? (any)  : ")
    for i in range(5):
        print("ready...{}".format(i))
        time.sleep(1)


    for i in range(page_count + 5) :
        Macro.mouse_click()
        time.sleep(1)
        Macro.capture_execute()

    with open("result/spec.spec", "wb") as f:
        pickle.dump(Macro.captureRect, f)
else:
    with open("result/spec.spec", "rb") as f:
        Macro.captureRect = pickle.load(f)
    Macro.crop_images()   



