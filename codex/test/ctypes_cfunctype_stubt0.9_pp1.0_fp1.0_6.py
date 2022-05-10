import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("Hello, world!")
    return 123
print("fun is:", fun)
fun()

print("="*30)
print("Python library API:")
