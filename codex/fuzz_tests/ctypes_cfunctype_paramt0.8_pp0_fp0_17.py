import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
libc = ctypes.CDLL('libc.so.6')

def callback():
    pass

cd = FUNTYPE(callback)

for i in range(200):
    print(libc.prctl(15, "0x%x" % id(cd), 0, 0, 0))
