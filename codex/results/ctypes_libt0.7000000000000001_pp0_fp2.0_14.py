import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import win32api
import win32con
import win32gui
import win32gui_struct
import wx

from wx.lib.buttons import GenBitmapButton


def get_monitor_dpi(hwnd=None):
    if hwnd:
        dc = win32gui.GetDC(hwnd)
    else:
        dc = win32gui.GetDC(0)
    ppix = win32gui.GetDeviceCaps(dc, win32con.LOGPIXELSX)
    ppiy = win32gui.GetDeviceCaps(dc, win32con.LOGPIXELSY)
    win32gui.ReleaseDC(hwnd, dc)
    return ppix, ppiy

# font size factor for scaling fonts based on DPI
# change this based on your own preference
FONT_SIZE_FACTOR = 2.0


def convert_to_dpi(size):
    return int(size * FONT_SIZE_FACTOR)


def convert_to_dpi_point
