import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)

def func_to_call(x):
    return math.sin(x)

def call_func_from_c(func):
    lib = ctypes.CDLL('./libm.so')
    f = FUNTYPE(func)
    lib.call_func_from_c.argtypes = [FUNTYPE]
    lib.call_func_from_c.restype = ctypes.c_double
    return lib.call_func_from_c(f)

call_func_from_c(func_to_call)
</code>
But this fails to compile with the following error:
<code>libm.c: In function ‘call_func_from_c’:
libm.c:5:6: error: incompatible type for argument 1 of ‘func’
  5 |   return func(x);
    |      ^~~~
    |      |
    |      double (*)(int)
makefile:2: recipe for target 'libm.o' failed
</code
