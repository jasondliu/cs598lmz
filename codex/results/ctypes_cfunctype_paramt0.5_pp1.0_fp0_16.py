import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int)

def callback(x):
    print 'callback:', x

def test():
    f = FUNTYPE(callback)
    f(42)

if __name__ == '__main__':
    test()
