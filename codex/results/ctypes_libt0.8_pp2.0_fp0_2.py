import ctypes
ctypes.windll.user32.UnlockWindowUpdate(h)

try:
    win32gui.SetForegroundWindow(hwnd)
except:
    pass
win32gui.EnumChildWindows(hwnd, foreach_window, None)
</code>
You can do it in two ways:
1. as a windows application
2. as a windows service

