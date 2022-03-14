from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

d = 2607
f = 2634 
j = 2718 
k = 2853 
y = 530



def click(x,y):
  win32api.SetCursorPos((x,y))
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
  time.sleep(0.01)
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while 1 == 1:
  if pyautogui.pixel(d,y)[0] == 1:
    click(d,y)
    print('d - click')
  if pyautogui.pixel(f,y)[0] == 1:
    click(f,y)
    print('f - click')
  if pyautogui.pixel(j,y)[0] == 1:
    click(j,y)
    print('j - click')
  if pyautogui.pixel(k,y)[0] == 1:
    click(k,y)
    print('k - click')
