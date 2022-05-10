import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)
def py_func(x):
  return x
CMPFUNC = FUNTYPE(py_func)

# now call the c code
from ctypes import *
#lib = cdll.LoadLibrary('./call_python_func.so')
# foo = lib.foo
foo = call_python_func.foo

# this call should fail (depends on the architecture)
try:
  foo(CMPFUNC(py_func), 0)
except:
  print('Cannot call function with function pointer returned from python')

# this call should succeed
foo(CMPFUNC(py_func), 1)


# now try the callback
print('now try the callback')
bar = call_python_func.bar
print('Calling bar with a callback')

# this cannot be called with default callback, but can be called with a callback
# returned from python
#bar(CMPFUNC(py_func))
print('Calling bar with a callback returned from python')
bar(CMPFUNC(py_func))
