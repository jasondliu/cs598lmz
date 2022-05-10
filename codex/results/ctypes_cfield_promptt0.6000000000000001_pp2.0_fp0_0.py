import ctypes
# Test ctypes.CField
class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [("s", S.CField),
                ("c", ctypes.c_int)]

# Test ctypes.CFuncPtr
libc = ctypes.CDLL(ctypes.util.find_library("c"))

# Test ctypes.CString
# Test ctypes.CStringError
# Test ctypes.CThunkObject
# Test ctypes.CThunkObjectError
# Test ctypes.CThunkObjectType
# Test ctypes.CThunkObjectTypeError
# Test ctypes.CVoidP
# Test ctypes.CVoidPtr
# Test ctypes.Cast
# Test ctypes.DllCanUnloadNow
# Test ctypes.DllGetClassObject
# Test ctypes.DllRegisterServer
# Test ctypes.DllUnregisterServer
# Test ctypes.FormatError
# Test ctypes.GetLastError
