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
        y=y-25
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
        t=2.5
        click(3319,962,t,1,1, mat='skip')
        click(3319,962,t,1,1, mat='skip again')
        while 1:
            click(2748,944,t,None, None, mat='Ability 1') #ability 1
            click(3684,861,t,1,1, mat='HIT') #enemy
            if (pag.pixel(3244,964) == (0, 0, 0)):
                break
            click(2794,947,t,None, None, mat='Ability 2') #ability 2
            click(3684,861,t,1,1, mat='HIT') #enemy
            if (pag.pixel(3244,964) == (0, 0, 0)):
                break
            click(2831,945,t,None, None, mat='Ability 3') #ability 3
            click(3684,861,t,1,1, mat='HIT') #enemy
            if (pag.pixel(3244,964) == (0, 0, 0)):
                break
            click(2874,942,t,None, None, mat='Ability 4') #ability 4
            click(3684,861,t,1,1, mat='HIT') #enemy
            if (pag.pixel(3244,964) == (0, 0, 0)):
                break
            click(3260,957,8,1,1, mat='SKIP') #skip turn


def ignore():
    if pag.pixel(1072+1920,557)[0] == 236:
        click(x=1,y=1,t=1,xx=None, yy=None, mat='Ignore')
        
def getColor(x: int,y: int, target: str) -> str:
    pxl_color = f'{target}: {pag.pixel(x, y)}'
    return pxl_color

def pickup(
    x: int ,
    y: int,
    c: tuple,
    t: int,
    x_clear: int or None,
    y_clear: int or None,
    display: str
    ) -> None:
    if pag.pixel(x, y) == c:
        click(x, y, t, x_clear, y_clear, display)
    fight()
    ignore()

            
def lago_cania_3M():
    t=6
    
    while keyboard.is_pressed('ctrl+q') == False:
        pickup(1396+1920, 356, (67, 67, 50), t, 1, 1, 'M7')
        pickup(1355+1920, 336, (74, 73, 52), t, 1, 1, 'M6')
        pickup(1307+1920, 314, (78, 76, 55), t, 1, 1, 'M5')
        pickup(959+1920, 470, (111, 89, 45), t, 1, 1, 'H4')
        pickup(2832, 492, (17, 52, 70), t, 1, 1, 'K3')
        pickup(869+1920, 514, (18, 57, 89), t, 1, 1, 'K2')
        pickup(826+1920, 535, (62, 50, 27), t, 1, 1, 'H1')
def main():
    print(getColor(1244, 964,'a'))

main()
