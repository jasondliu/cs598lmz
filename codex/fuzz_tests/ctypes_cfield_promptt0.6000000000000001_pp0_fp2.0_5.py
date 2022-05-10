import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

class RECT(ctypes.Structure):
    _fields_ = [("origin", POINT), ("size", POINT)]

r = RECT()
r.origin.x = 5
r.origin.y = 10
r.size.x = 15
r.size.y = 20

print(r.origin.x)
print(r.origin.y)
print(r.size.x)
print(r.size.y)
# Test ctypes.c_char_p
libc = ctypes.CDLL(None)

message_string = b"Hello world!\n"
libc.printf("Testing: %s", message_string)

# Test ctypes.Union
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

class RECT(ctypes.Structure):

