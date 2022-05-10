import gc, weakref
import ctypes
from ctypes import wintypes

from win32com import client
from win32com.client import constants

from win32com.client import Dispatch
from win32com.client import constants
from win32com.client import gencache

import win32com.client
import win32gui
import win32api
import win32con

import pythoncom
import pywintypes

import win32com.client.gencache

import sys

import time

#def get_hwnds_for_pid(pid):
#    def callback (hwnd, hwnds):
#        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
#            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
#            if found_pid == pid:
#                hwnds.append(hwnd)
#        return True
#    hwnds = []
#    win32gui.EnumWindows(callback, hwnds)
#    return hwnds

