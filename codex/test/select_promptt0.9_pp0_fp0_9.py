import select
# Test select.select()
# Replace get_constants() with the following lines

for name in dir(select):
    if name.startswith('EPOLL') or name.startswith('POLL'):
        print(name)

import socket
from socket import *

socket_names = dir(socket)

print(socket_names)
