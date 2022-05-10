import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print "hello"

if __name__ == "__main__":
    fun()
</code>

