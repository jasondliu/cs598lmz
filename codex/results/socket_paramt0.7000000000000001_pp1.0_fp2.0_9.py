import socket
socket.if_indextoname(1)

socket.if_nameindex()

import sys
sys.getwindowsversion()

sys.winver

sys.getdefaultencoding()

sys.getfilesystemencoding()

sys.getrecursionlimit()

sys.setrecursionlimit(100)

sys.getrecursionlimit()

sys.getrefcount(100)

a = 100
sys.getrefcount(a)

b = 100
sys.getrefcount(a)

sys.getprofile()

sys.setprofile(None)

sys.getprofile()

sys.getsizeof(123)

sys.getsizeof(True)

sys.getsizeof(None)

sys.getsizeof(b'123')

sys.getsizeof('123')

sys.getsizeof([1,2,3])

import pprint

pprint.pprint([1,2,3])

import platform

platform.platform()

platform.architecture()
platform.machine()
platform.node()
platform.processor()
