import ctypes
# Test ctypes.CFUNCTYPE
def cb(x):
    print "cb(",x,")"

f = ctypes.CFUNCTYPE(None, ctypes.c_int)(cb)
f(1)

print "Test ctypes.CFUNCTYPE with result"
def cb(x):
    print "cb(",x,")"
    return 1

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(cb)
print f(1)

print "Test ctypes.CFUNCTYPE with error"
def cb(x):
    print "cb(",x,")"
    raise ValueError

f = ctypes.CFUNCTYPE(None, ctypes.c_int)(cb)
try:
    f(1)
except ValueError:
    pass

print "Test ctypes.CFUNCTYPE with more args"
def cb(*args):
    print "cb(",args,")"

f = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes
