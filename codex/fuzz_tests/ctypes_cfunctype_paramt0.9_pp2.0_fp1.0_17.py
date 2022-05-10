import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

function = FUNTYPE(idivmod)

print function(100.0, 5.0)


p = PyCFunction_New(function, None)
python_function = PyCFunction_GetFunction(p)
print python_function(100, 5)

c_function = cast(python_function, FUNTYPE).value
print c_function(100, 5)


c_function = cast(callable, FUNTYPE).value
print c_function(100, 5)
