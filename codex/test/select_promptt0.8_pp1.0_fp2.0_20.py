import select
# Test select.select, and select.unselect
# with datagram protocol

import socket
import time

# create datagram sockets

s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

