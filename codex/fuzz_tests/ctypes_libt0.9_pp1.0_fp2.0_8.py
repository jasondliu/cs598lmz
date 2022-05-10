import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)


from pathlib import Path
import re
import subprocess
import win32api, win32con, win32ui
from win32api import GetSystemMetrics
import win32com.client
from win32gui import FindWindow, FindWindowEx, GetClassName
import os


class Utils:

    @staticmethod
    def check_windows_10():
        is_windows_10 = True #Has to be True until we test with lower version of Windows
        return is_windows_10

    @staticmethod
    def get_curent_window():
        current_window = win32gui.GetForegroundWindow()
        return current_window

    @staticmethod
    def is_curent_window_command():
        current_window = win32gui.GetForegroundWindow()
        current_window_name = win32gui.GetWindowText(current_window)
        if current_window_name == 'Command Prompt':
            return True
        return False

    @staticmethod
    def get
