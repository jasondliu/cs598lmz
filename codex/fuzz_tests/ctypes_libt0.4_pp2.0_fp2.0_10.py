import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import win32api
win32api.MessageBox(0, "Your text", "Your title")

import win32gui
win32gui.MessageBox(0, "Your text", "Your title")
</code>

