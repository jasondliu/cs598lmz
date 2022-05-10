import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

#
#   WLMGetWindowInfo()
#

def WLMGetWindowInfo(hWnd):
    ai = WINDOWINFO()
    if not user32.GetWindowInfo(hWnd, ctypes.byref(ai)):
        raise ctypes.WinError()
    return ai

#
#   GetWindowPlacement()
#

def GetWindowPlacement(hWnd):
    ai = WINDOWPLACEMENT()
    if not user32.GetWindowPlacement(hWnd, ctypes.byref(ai)):
        raise ctypes.WinError()
    return ai

#
#   GetWindowRect()
#

def GetWindowRect(hWnd):
    ai = RECT()
    if not user32.GetWindowRect(hWnd, ctypes.byref(ai)):
        raise ctypes.WinError()
    return ai

#
#   GetMonitorInfo()
#

def GetMonitorInfo(hMonitor):
    ai = MON
