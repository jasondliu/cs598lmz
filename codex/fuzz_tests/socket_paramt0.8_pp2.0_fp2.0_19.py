import socket
socket.if_indextoname("wlan0")

import os
os.system("ip addr show wlan0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1")

import subprocess
subprocess.run("ip addr show wlan0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1", shell=True)

import psutil
[i for i in psutil.net_if_addrs().items() if i[0][0] != "e"]
[i for i in psutil.net_if_addrs().items() if i[0] == "wlan0"]
[i for i in psutil.net_if_addrs().items() if i[0] == "wlan0"][0][1][0][1]

import platform
print(platform.system())
print(platform.release())
print(platform.version())

import os
os.system("uname -o")
os.system("uname -r")

import subprocess
subprocess.run("uname -o", shell
