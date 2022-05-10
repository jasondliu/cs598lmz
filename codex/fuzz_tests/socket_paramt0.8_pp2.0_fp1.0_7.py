import socket
socket.if_indextoname(2)

#FAST
socket.if_indextoname = lambda i: 'vmnet8'
socket.if_indextoname(2)

import socket
socket.if_indextoname = lambda i: 'vmnet8'

#FAST
import ctypes
socket.if_indextoname = ctypes.pythonapi.PyString_FromString
socket.if_indextoname.restype = ctypes.py_object
socket.if_indextoname = lambda x: socket.if_indextoname('vmnet8')
socket.if_indextoname(2)

#FAST
import ctypes
socket.if_indextoname = ctypes.pythonapi.PyString_FromString
socket.if_indextoname.restype = ctypes.py_object
socket.if_indextoname = lambda x: 'vmnet8'
socket.if_indextoname(2)

#SLOW
import ctypes
socket.if_indextoname = ctypes.pythonapi.PyString_FromString
