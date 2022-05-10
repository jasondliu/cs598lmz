import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int)

def callback(n):
    print 'callback', n

f = FUNTYPE(callback)

print f(1)
print f(2)
</code>

