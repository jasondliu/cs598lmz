import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def main():
    print(fun())

if __name__ == '__main__':
    main()
