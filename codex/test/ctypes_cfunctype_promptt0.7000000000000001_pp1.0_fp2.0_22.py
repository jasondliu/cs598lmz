import ctypes
# Test ctypes.CFUNCTYPE()
def test():
    print(123)

CBFUNC = ctypes.CFUNCTYPE(None)

cbf = CBFUNC(test)
cbf()

if __name__ == '__main__':
    pass
