import socket
socket.if_indextoname('46')

import ctypes

libc = ctypes.CDLL('libc.dylib')
libc.if_indextoname('46')

libc.if_indextoname(46)

import ctypes
ctypes.cdll.LoadLibrary('libSystem.dylib')

import socket
