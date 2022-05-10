import socket
socket.if_indextoname(3)

import platform
print(platform.system())
print(platform.release())
print(platform.version())
print(platform.machine())
print(platform.processor())
print(platform.uname())

import os
print(os.uname())

import time
print(time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.ctime())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

import sys
print(sys.version)
print(sys.version_info)
print(sys.platform)
print(sys.stdout.encoding)
print(sys.path)

import psutil
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.cpu_times())
print(psutil.cpu_percent(interval=1, percpu=True))
print(psutil.virtual
