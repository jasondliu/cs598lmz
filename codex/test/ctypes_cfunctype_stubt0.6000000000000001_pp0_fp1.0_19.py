import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello World"

def fun2():
    return "Hello World"

if __name__ == '__main__':
    print(fun())
    print(fun2())
