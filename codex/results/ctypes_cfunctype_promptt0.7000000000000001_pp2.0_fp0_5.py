import ctypes
# Test ctypes.CFUNCTYPE

# This should work.
def callback(*args):
    pass

callback = ctypes.CFUNCTYPE(None)(callback)


# This should also work.
x = ctypes.CFUNCTYPE(None)(lambda: None)

# This should also work.
def callback(*args):
    return None

def callback2(*args):
    return ctypes.c_int(42)

callback = ctypes.CFUNCTYPE(None)(callback)
callback2 = ctypes.CFUNCTYPE(ctypes.c_int)(callback2)

x = ctypes.CFUNCTYPE(None)(lambda: None)
y = ctypes.CFUNCTYPE(ctypes.c_int)(lambda: ctypes.c_int(42))

# These should raise a TypeError
try:
    ctypes.CFUNCTYPE(None)(lambda x: None)
except TypeError:
    print "exception 1 passed"

try:
    ctypes.CFUNCTYPE(None)(lambda: None, None)
except
