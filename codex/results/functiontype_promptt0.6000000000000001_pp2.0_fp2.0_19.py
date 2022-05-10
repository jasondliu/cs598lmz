import types
# Test types.FunctionType
def f(a, b):
    """Just a function"""
    return a < b

assert type(f) is types.FunctionType
assert type(f).__name__ == 'function'
assert type(f).__module__ == 'types'
assert f.__name__ == 'f'
assert f.__doc__ == 'Just a function'
assert f.__defaults__ == ()
assert f.__code__.co_argcount == 2
assert f.__code__.co_varnames == ('a', 'b')
# Test types.BuiltinFunctionType
assert type(abs) is types.BuiltinFunctionType
assert type(abs).__name__ == 'builtin_function_or_method'
assert type(abs).__module__ == 'builtins'
assert abs.__name__ == 'abs'
assert abs.__doc__ is not None
assert abs.__code__ is None
assert abs.__defaults__ is None
assert abs.__globals__ is None
assert abs.__dict__ is None
# Test types.LambdaType
f =
