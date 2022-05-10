import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\a')).start()

# Windows
import ctypes
ctypes.windll.user32.MessageBoxA(None, 'hello world', 'Title', 0)

# dnotify (Linux)
import os, sys, select
dnotify = os.open('.', os.O_RDONLY)
os.fcntl(dnotify, F_SETSIG, 0)
os.fcntl(dnotify, F_NOTIFY, DN_MODIFY|DN_CREATE|DN_DELETE|DN_RENAME|DN_ATTRIB)

# Watchman
import pywatchman
c = pywatchman.Client()
c.query('watch', '.')
