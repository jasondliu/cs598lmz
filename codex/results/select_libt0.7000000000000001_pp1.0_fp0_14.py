import select
import socket
import sys
import os

import struct
import time

try:
	import fcntl
except:
	pass

import xlog
import v2ray_io
import v2ray_protocol_pb2 as v2ray_pb

def set_nonblocking(sock):
	if os.name == 'nt':
		sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
	else:
		flags = fcntl.fcntl(sock, fcntl.F_GETFL)
		fcntl.fcntl(sock, fcntl.F_SETFL, flags | os.O_NONBLOCK)

def set_blocking(sock):
	if os.name == 'nt':
		sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
	else:
		flags = fcntl.fcntl(sock, fcntl.F_GETFL)
		
