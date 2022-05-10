import types
# Test types.FunctionType
def f():
    return 0
f.__name__ = 'f'
f.__doc__ = 'f() -> 0'
f.__dict__ = {'a': 1, 'b': 2}
f.__defaults__ = (1,)
f.__closure__ = (1,)
f.__code__ = types.CodeType(
    0, 0, 0, 0, '', (), (), (), '', '', 0, '', (), (), ())
f.__globals__ = {}
f.__dict__ = {'a': 1, 'b': 2}
f.__module__ = 'm'

# Test types.BuiltinFunctionType
def f():
    return 0
f.__name__ = 'f'
f.__doc__ = 'f() -> 0'
f.__dict__ = {'a': 1, 'b': 2}
f.__module__ = 'm'

# Test types.MethodType
def f():
    return 0
f.__name__ = 'f'
f.__doc__ = 'f() -> 0'

