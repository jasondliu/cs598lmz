import ctypes
ctypes.cast(0, ctypes.py_object)

import sys, ctypes
from ctypes import wintypes

user32 = ctypes.WinDLL('user32', use_last_error=True)

HWND_BROADCAST = 0xFFFF

WM_SETTINGCHANGE = 0x001A

SMTO_ABORTIFHUNG = 0x0002

ERROR_TIMEOUT = 1460

class SIZE(ctypes.Structure):
    _fields_ = (('cx', wintypes.LONG),
                ('cy', wintypes.LONG))

def broadcast_system_metrics_change():
    size = SIZE()
    user32.SystemParametersInfoW(0x0002, 0, ctypes.byref(size), 0)
    assert user32.GetLastError() == 0

    result = user32.SendNotifyMessageW(HWND_BROADCAST, WM_SETTINGCHANGE,
                                       0, 'DisplayChange')
    assert result != 0 or user32.GetLastError() in (ERROR_TIMEOUT, 0
