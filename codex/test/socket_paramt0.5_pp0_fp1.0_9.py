import socket
socket.if_indextoname(3)

import os
os.system("ifconfig en0 | grep 'inet '")

import psutil
psutil.net_if_addrs()

psutil.net_if_stats()

# https://docs.python.org/3/library/socket.html
# https://docs.python.org/3/library/os.html
# https://psutil.readthedocs.io/en/latest/
# https://psutil.readthedocs.io/en/latest/#network
