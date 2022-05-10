import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("Hello")
    return "Hello"

def main():

    fun()
    print(type(fun))

if __name__ == '__main__':
    main()
