import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    # Avoiding a global, in case the code that calls this
    # function is running in a restricted environment.
    import sys, os
    f = sys._getframe(1)
    return f.f_code.co_filename, f.f_lineno
c = compile("""
def f():
    return fun()
""", "", "exec")
eval(c)
print f()
</code>

