import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  return 42

print(fun())
</code>
This works, but I am not sure if it is the best way to do this.

