import cv2 
import os


def crop_images():
    read_num = 0
    while True:
        print(read_num)
        dir = "result/{}.png".format(read_num)
        if os.path.exists(dir) == False:
            break
        img = cv2.imread(dir, cv2.IMREAD_GRAYSCALE)

        img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C ,cv2.THRESH_BINARY,15,5)
        cv2.imwrite(dir, img)  
        read_num += 1

crop_images()