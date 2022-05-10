import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __getattr__(self, name):
        return getattr(ctypes, name)

c = C()

def f():
    "Docstring"
    pass

print 'f.__doc__ =', f.__doc__
print 'f.__name__ =', f.__name__
print 'f.__module__ =', f.__module__
print 'f.__dict__ =', f.__dict__
print 'f.__defaults__ =', f.__defaults__
print 'f.__code__ =', f.__code__
print 'f.__globals__ =', f.__globals__
print 'f.func_closure =', f.func_closure
print 'f.func_code =', f.func_code
print 'f.func_defaults =', f.func_defaults
print 'f.func_dict =', f.func_dict
print 'f.func_doc =', f.func_doc
print 'f.func_globals =', f.func_
