import ctypes
# Test ctypes.CFUNCTYPE

@ctypes.CFUNCTYPE(None)
def func():
    return 1

# @ctypes.WINFUNCTYPE(None)
@ctypes.WINFUNCTYPE(ctypes.c_int)
def func2():
    return 1

# @ctypes.CFUNCTYPE(None, ctypes.c_int)
@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def func3(a, b):
    return a + b

def func4():
    print("func4")

@ctypes.CFUNCTYPE(None)
def func5():
    print("func5")

f = func5
f()

# CFUNCTYPE(None)
# CFUNCTYPE(ctypes.c_int)
# CFUNCTYPE(None, ctypes.c_int)
# CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
#
