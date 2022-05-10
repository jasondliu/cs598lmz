fn = lambda: None
# Test fn.__code__
d = {'x': 1}
e = {'y': 2}
f = fn._getframe(1)
if verbose > 2:
    print f.f_code, f.f_code.co_name, f.f_code.co_filename, f.f_code.co_firstlineno
    print f.f_code.co_varnames
    print f.f_code.co_argcount
    print f.f_code.co_names
    print f.f_code.co_nlocals
    print f.f_code.co_stacksize
# Test fn.__globals__
if verbose:
    print f.f_globals
    print d
    print f.f_globals == d
# Test fn.__closure__
fn.__closure__ = (d,)
if verbose:
    print fn.__closure__
    print d
    print fn.__closure__[0] is d
# Test fn.func_code
if verbose:
    print fn.func_code
    print
