import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print('hello world')
    return None

def main():
    fun()
    return 0

if __name__ == '__main__':
    main()
