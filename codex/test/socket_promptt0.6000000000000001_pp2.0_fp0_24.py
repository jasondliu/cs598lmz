import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))

import os
# Test os.getlogin()
print(os.getlogin())

import time
# Test time.tzset()
time.tzset()

import random
# Test random.SystemRandom
random.SystemRandom()

import _ssl
# Test _ssl.enum_certificates()
for cert in _ssl.enum_certificates("SYSTEM"):
    print(cert)

from _multiprocessing import SemLock
# Test SemLock
SemLock()

from queue import Queue
# Test Queue.mutex
Queue().mutex

import _tkinter
# Test _tkinter.create()
_tkinter.create()

import _scproxy
# Test _scproxy._get_proxy_settings()
_scproxy._get_proxy_settings()

import _winreg
# Test _winreg.OpenKeyEx()
_winreg.OpenKeyEx(None, "")

import win32api
# Test win32api.GetCursorPos()
