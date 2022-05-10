import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import win32gui
win32gui.MessageBox(None, 'Your text', 'Your title', 1)
</code>

