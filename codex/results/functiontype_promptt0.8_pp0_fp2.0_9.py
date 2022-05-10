import types
# Test types.FunctionType()
try:
    f = types.FunctionType(lambda x:x, globals(), 'test')
    if (callable(f) and
        f.__name__ == 'test' and
        f.__module__ is None and
        f.__doc__ is None and
        f.__defaults__ is None and
        f.__code__ is f.__closure__ is None and
        f.__dict__ is None and
        f(1) == 1):
        pass
    else:
        raise TestFailed, 'types.FunctionType()'
except (TypeError, AttributeError):
    raise TestFailed, 'types.FunctionType()'

# Test types.MethodType()
import types, sys
def f(): pass
f_func = f.__func__
f_self = f.__self__
m = types.MethodType(f_func, f_self)
if (callable(m) and
    m.__doc__ is f_func.__doc__ and
    m.__name__ == f_func.__name__ and
   
