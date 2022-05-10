import ctypes
ctypes.windll.user32.EnumWindows(callback, None)
