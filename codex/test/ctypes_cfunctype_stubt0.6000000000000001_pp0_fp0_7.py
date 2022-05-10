import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

fun.__name__ = 'test'

def main():
    pass

if __name__ == '__main__':
    main()
