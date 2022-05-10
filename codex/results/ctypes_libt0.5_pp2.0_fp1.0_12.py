import ctypes
ctypes.windll.user32.MessageBoxW(0, 'hello', 'hello', 0)

# For Python 3.x use 'win32api'
import win32api
win32api.MessageBox(0, 'hello', 'hello')

# For Python 2.x use 'win32gui'
import win32gui
win32gui.MessageBox(0, 'hello', 'hello', 0)
</code>

