import pyautogui as pag
import time
import keyboard
import numpy as np
import random
import win32api, win32con
import autoit
import datetime

hora = datetime.datetime.now()
game_version = 'Hiperthreias - Dofus 2.73.3.2'

def click(x: int,y: int,t: int, xx: int|None, yy: int|None, mat: str|None):
    autoit.control_click(
        game_version,
        "",
        text="",
        button='left',
        clicks=1,
        x=x-1920,
        y=y-40
        ),
    if mat:
        print(mat)
    if xx is not None:
        autoit.control_click(
            game_version,
            "",
            text="",
            button='left',
            clicks=1,
            x=xx,
            y=yy,
            )
    time.sleep(t)

def fight():        
    
    if pag.pixel(3244, 964) == (206, 240, 0): ##TODO: click challenge
        t=1.5
        click(1399,962,t,1,1, mat='skip')
        click(1399,962,t,1,1, mat='skip again')
        while 1:
            click(828,944,t, mat='Ability 1') #ability 1
            click(1764,861,t,1,1, mat='HIT') #enemy
            if (pag.pixel(3244,964) != (206, 240, 0) or pag.pixel(3244,964) != (123, 143, 0)):
                break
            click(874,947,t, mat='Ability 2') #ability 2
            click(1764,861,t,1,1, mat='HIT') #enemy
            if (pag.pixel(3244,964) != (206, 240, 0) or pag.pixel(3244,964) != (123, 143, 0)):
                break
            click(911,945,t, mat='Ability 3') #ability 3
            click(1764,861,t,1,1, mat='HIT') #enemy
            if (pag.pixel(3244,964) != (206, 240, 0) or pag.pixel(3244,964) != (123, 143, 0)):
                break
            click(954,942,t, mat='Ability 4') #ability 4
            click(1764,861,t,1,1, mat='HIT') #enemy
            if (pag.pixel(3244,964) != (206, 240, 0) or pag.pixel(3244,964) != (123, 143, 0)):
                break
            click(1340,957,5,1,1, mat='SKIP') #skip turn


def ignore():
    if pag.pixel(1072+1920,557)[0] == 236:
        click(x=1,y=1,t=1, mat='Ignore')
        
def getColor(x: int,y: int, target: str):
    print(f'{target}: {pag.pixel(x, y)}')

def pickup(x,y,c, t, x_clear, y_clear, display):
    if pag.pixel(x, y) == c:
        click(x, y, t, x_clear, y_clear, display)
    fight()
    ignore()

            
def lago_cania_3M():
    t=5
    
    while keyboard.is_pressed('ctrl+q') == False:
        pickup(1396+1920, 356, (67, 67, 50), t, 1, 1, 'M7')
        pickup(1355+1920, 336, (74, 73, 52), t, 1, 1, 'M6')
        pickup(1307+1920, 314, (78, 76, 55), t, 1, 1, 'M5')
        pickup(959+1920, 470, (111, 89, 45), t, 1, 1, 'H4')
        pickup(2832, 492, (17, 52, 70), t, 1, 1, 'K3')
        pickup(869+1920, 514, (18, 57, 89), t, 1, 1, 'K2')
        pickup(826+1920, 535, (62, 50, 27), t, 1, 1, 'H1')




def main():
    print(hora)
    #getColor(3244, 964,'a')
    lago_cania_3M()



main()
