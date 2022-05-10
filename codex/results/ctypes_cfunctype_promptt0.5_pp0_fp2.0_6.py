import ctypes
# Test ctypes.CFUNCTYPE
def test_cfunc(a, b):
    return a + b

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(a, b):
    return a + b

c_callback = CALLBACK(callback)

print(c_callback(1, 2))
print(test_cfunc(1, 2))

# Test ctypes.POINTER

class POINTER(object):
    def __init__(self, x):
        self.x = x
    def contents(self):
        return self.x

def test_pointer(p):
    return p.contents()

p = POINTER(1)

print(test_pointer(p))
