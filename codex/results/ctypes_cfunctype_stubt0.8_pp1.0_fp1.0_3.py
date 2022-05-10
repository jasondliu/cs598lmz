import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  return "hello"

print(fun())
</code>
or, if <code>fun</code> is a free function:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  return "hello"

LIB = ctypes.CDLL("foolib.so")
LIB.fun = fun
</code>

