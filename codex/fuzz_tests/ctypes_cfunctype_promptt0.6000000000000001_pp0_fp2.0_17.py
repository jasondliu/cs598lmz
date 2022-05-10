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

CreateFileW = windll.kernel32.CreateFileW
CreateFileW.argtypes = [
    c_wchar_p, c_uint32, c_uint32, SECURITY_ATTRIBUTES_P, c_uint32,
    c_uint32, c_void_p]
CreateFileW.restype = c_void_p

def test_createfile():
    sa = SECURITY_ATTRIBUTES()
    sa.nLength = sizeof(sa)
    handle = CreateFileW(u"C:\\test
