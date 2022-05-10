import types
# Test types.FunctionType
def f(x):
    return x+1

assert isinstance(f, types.FunctionType)
assert issubclass(types.FunctionType, object)

assert f.__name__ == 'f'
assert f.__qualname__ == 'f'
assert f.__annotations__ == {}
assert f.__code__.co_name == 'f'
assert f.__code__.co_varnames == ('x',)
assert f.__code__.co_argcount == 1
assert f.__code__.co_flags == 67
assert f.__code__.co_filename == '<stdin>'
assert f.__code__.co_firstlineno == 1
assert f.__code__.co_lnotab == b'\x00\x01\x0a\x00'
assert f.__code__.co_freevars == ()
assert f.__code__.co_cellvars == ()
assert f.__code__.co_consts == (None,)

assert f.__closure__ is None
assert f.
