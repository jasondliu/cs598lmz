import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def f():
    return 'world'

print(fun.__closure__)
# (None,)
fun.__closure__ = (f,)
print(fun.__closure__)
# (<cell at 0x10b70fbc8: function object at 0x10b68f428>,)
f()
# 'world'
fun()
# 'world'
fun.__closure__[0].cell_contents()
# 'world'
fun.__closure__[0].cell_contents
# <function f at 0x10b68f428>
