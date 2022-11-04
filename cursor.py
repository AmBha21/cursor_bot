import pyautogui as pag
import random
import time




while True:
    x = random.randint(500,1000)
    y = random.randint(200,800)
    pag.moveTo(x,y,0.2)
    time.sleep(5)


