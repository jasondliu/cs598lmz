import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# import os
# os.system('C:\Windows\System32\mspaint.exe')

import subprocess as sp

sp.Popen('C:\Windows\System32\mspaint.exe')
