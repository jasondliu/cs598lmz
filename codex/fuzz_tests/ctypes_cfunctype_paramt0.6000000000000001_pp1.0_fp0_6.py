import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(x, y):
    print 'x=%s, y=%s' % (x, y)
    return x + y

mylib = ctypes.CDLL('mylib.dll')
# mylib = ctypes.CDLL('./mylib.so')
mylib.add.argtypes = [ctypes.c_int, ctypes.c_int]
mylib.add.restype = ctypes.c_int
mylib.add.errcheck = callback

print mylib.add(1, 2)
</code>

