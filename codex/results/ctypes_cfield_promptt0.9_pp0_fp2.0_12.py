import ctypes
# Test ctypes.CField() 
# Quaal: https://docs.python.org/3/library/ctypes.html#cfield-objects

class POINT(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int)
    ]

    def __repr__(self):
        return "x: " + str(self.x) + ",y: " + str(self.y)

def handler(signum, frame):
    print("Inside handler!")

point = POINT()
point.x = 40
point.y = 100

handler_sigabrt = ctypes.CFUNCTYPE(None)(handler)
print(handler_sigabrt, type(handler_sigabrt))

print(point)

print(ctypes.CFUNCTYPE(ctypes.c_int)(lambda: 1))

# https://stackoverflow.com/questions/37849705/error-use-with-swig-ctypes-and-sigabrt-
