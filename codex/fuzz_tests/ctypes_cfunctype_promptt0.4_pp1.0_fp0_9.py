import ctypes
# Test ctypes.CFUNCTYPE

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def add(a, b):
    return a + b

print add(1, 2)

# Test ctypes.POINTER

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

Point = ctypes.POINTER(POINT)

p = Point()
p.contents = POINT(1, 2)
print p.contents.x, p.contents.y

# Test ctypes.byref

p = Point()
p.contents = POINT(1, 2)
print p.contents.x, p.contents.y

def add_point(p):
    p.contents.x += 1
    p.contents.y += 1

add_point(p)
print p.contents.x, p.contents.y

# Test ctypes.
