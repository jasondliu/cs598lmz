import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def main():
    print(fun())

if __name__ == '__main__':
    main()
</code>

