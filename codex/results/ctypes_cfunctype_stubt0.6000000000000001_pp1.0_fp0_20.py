import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print 'in fun()'
    return 42
print fun()
</code>
If you want to call C code from Python you need to write a C extension module. This is not trivial, but there are a number of tutorials available.

