import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello, World!"

ctypes.pythonapi.PyEval_EvalCode(ctypes.py_object(fun.__code__).value, globals(), globals())

print(fun())

# Output:
# Hello, World!
</code>
It's kinda hacky, I know, but it works.

