import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import os
os.system("msg * hello")
