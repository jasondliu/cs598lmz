import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

#import win32api
#win32api.MessageBox(0, 'Python 你好！', '你好', win32con.MB_OK)

import win32gui
import win32con
win32gui.MessageBox(0, 'Python 你好！', '你好', win32con.MB_OK)
