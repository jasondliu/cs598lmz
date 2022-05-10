import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import pywinauto
pywinauto.Desktop(backend='uia').window(title='Login to Server').child_window(title="Button", control_type="Button").click()
