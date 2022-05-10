import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import sys, os
import win32api, win32con
import win32gui
import time

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def get_pos(x1,y1,x2,y2):
    hwnd = win32gui.FindWindow(None, "Paint")
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0] + x1
    y = rect[1] + y1
    win32api.SetCursorPos((x,y))
    time.sleep(1)
    x,y = win32api.GetCursorPos()
    return x,y

