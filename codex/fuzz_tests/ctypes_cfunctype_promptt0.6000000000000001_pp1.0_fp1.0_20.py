import ctypes
# Test ctypes.CFUNCTYPE()

import sys
import inspect

from ctypes import *

if sys.platform == "win32":
    libc = cdll.msvcrt
else:
    libc = cdll.LoadLibrary(None)

print(type(libc._getpid))
print(libc._getpid)
print(libc._getpid())
# <class 'ctypes.CDLL'>
# <_FuncPtr object at 0x7fafb71e0b48>
# 11984

# <class 'ctypes._CFuncPtr'>
# <_FuncPtr object at 0x7fafb71e0b48>
# 11984

# <class 'ctypes._CFuncPtr'>
# <_FuncPtr object at 0x7fafb71e0b48>
# 11984

# <class 'ctypes._CFuncPtr'>
# <_FuncPtr object at 0x7fafb71e0b48>
# 11984
