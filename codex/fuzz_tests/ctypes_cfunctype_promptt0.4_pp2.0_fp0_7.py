import ctypes
# Test ctypes.CFUNCTYPE

def func(a):
    print a

f = ctypes.CFUNCTYPE(None, ctypes.c_int)(func)
f(42)
# Test ctypes.PYFUNCTYPE

def func(a):
    print a

f = ctypes.PYFUNCTYPE(None, ctypes.c_int)(func)
f(42)
# Test ctypes.WINFUNCTYPE

def func(a):
    print a

f = ctypes.WINFUNCTYPE(None, ctypes.c_int)(func)
f(42)
# Test ctypes.c_int.from_address()

addr = ctypes.addressof(ctypes.c_int(42))
print ctypes.c_int.from_address(addr).value
# Test ctypes.c_int.in_dll()

ctypes.c_int.in_dll(ctypes.cdll.msvcrt, "errno").value
# Test ctypes.c_int.from_param()

def func
