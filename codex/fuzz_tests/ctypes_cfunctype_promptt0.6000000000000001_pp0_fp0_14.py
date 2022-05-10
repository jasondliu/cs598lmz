import ctypes
# Test ctypes.CFUNCTYPE
def callback(n):
    return n * 2
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
# Test ctypes.POINTER
CALLBACKP = ctypes.POINTER(CALLBACK)
# Test ctypes.cast
c_callback = CALLBACK(callback)
c_callbackp = ctypes.cast(c_callback, CALLBACKP)
assert c_callbackp[0](41) == callback(41) == 82
# Test ctypes.c_int.in_dll()
dll = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))
c_int = ctypes.c_int.in_dll(dll, 'errno')
c_int.value = 123
assert c_int.value == 123
# Test ctypes.c_int(123).value
assert ctypes.c_int(123).value == 123
# Test ctypes.c_int.from_address()
assert ctypes.c_int.from_address(id(c_int)).
