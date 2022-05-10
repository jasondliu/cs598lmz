import socket
# Test socket.if_indextoname
print([socket.if_indextoname(z) for z in socket.if_nametoindex.keys()])

import _thread
import threading
# Test threading
print(threading.enumerate())

import struct
# Test struct
print(struct.calcsize("10s"))

import sys
# Test sys
print(sys.float_info)
print(sys.int_info)

import os
# Test os
print(os.getegid())
print(os.getgroups())
print(os.uname())

import array
import _collections

import operator
import cmath
import math
# Test math
print(math.log(42))
print(math.fabs(-42))
print(math.acos(1))
print(math.atan2(1, 2))
print(math.ceil(math.pi))
print(math.sinh(0))
print(math.copysign(3, 1))
print(math.log10(1000))
print(math.hypot(3, 4))
print
