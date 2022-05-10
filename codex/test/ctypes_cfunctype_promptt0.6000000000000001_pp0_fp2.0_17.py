import ctypes
# Test ctypes.CFUNCTYPE (Structure)
# http://msdn.microsoft.com/en-us/library/ms680573.aspx
from ctypes import *
class SECURITY_ATTRIBUTES(Structure):
    _fields_ = [
        ('nLength', c_int),
        ('lpSecurityDescriptor', c_void_p),
        ('bInheritHandle', c_int)
    ]

SECURITY_ATTRIBUTES_P = POINTER(SECURITY_ATTRIBUTES)

