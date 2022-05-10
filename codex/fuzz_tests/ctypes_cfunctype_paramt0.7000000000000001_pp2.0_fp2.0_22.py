import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.c_int, ctypes.c_int)
</code>
However, I don't like this solution because it doesn't allow me to return complex objects, and I cannot pass complex objects as arguments either.
Using <code>ctypes.py_object</code> as a return type is bad, because the python interpreter will crash, if the return value is a non-basic type (e.g. a numpy array), due to an error in the garbage collector.
Does anyone know a way of doing this in python?


A:

You could create a class that wraps the function pointer, and expose it to Python code as an object.
<code>class FunctionPointerWrapper(object):
    def __init__(self, function_pointer):
        self._function_pointer = function_pointer

    def __call__(self, *args):
        return self._function_pointer(*args)

# ...
for name in dir(functions_module):
    if callable(getattr(functions_module, name)):
        setattr(functions_module, name,
