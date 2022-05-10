import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

f = fun()            # or b.f = fun
print f(b)           # 42
print b.f()          # 42
print b.g(1)         ## Exception AttributeError: 'ctin' object has no attribute 'g'
</code>

