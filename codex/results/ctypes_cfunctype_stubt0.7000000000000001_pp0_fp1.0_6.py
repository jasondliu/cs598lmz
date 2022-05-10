import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return len

def main():
    f = fun()
    print f([1,2,3])

main()
</code>

