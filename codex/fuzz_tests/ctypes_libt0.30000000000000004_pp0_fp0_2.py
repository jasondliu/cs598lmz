import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

import os
os.system('msg * "Hello world"')

import subprocess
subprocess.call(['msg', '*', 'Hello world'])

import win32api
win32api.MessageBox(0, 'Hello world', 'Title')
</code>

