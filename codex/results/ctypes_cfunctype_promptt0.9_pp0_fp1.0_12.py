import ctypes
# Test ctypes.CFUNCTYPE
#@ctypes.CFUNCTYPE(None)
def test():
    print("hello")

#test() 

#cfuntype = ctypes.CFUNCTYPE(ctypes.c_long, ctypes.c_long)
#error: use ctypes.CFUNCTYPE
#argtypes = [ctypes.c_long, ctypes.c_long]
#func = cfuntype(*argtypes)
add = ctypes.CFUNCTYPE(ctypes.c_long, ctypes.c_long, ctypes.c_long)(lambda a, b: a+b)
assert add(1, 2) == 3, \
    "Error: add is not valid! %s" % add
print ("add is Ok.")

sub = ctypes.CFUNCTYPE(ctypes.c_long, ctypes.c_long, ctypes.c_long)(lambda a, b: a-b)
assert sub(3, 1) == 2, \
    "Error: sub is not valid! %s" % sub
print ("sub is
