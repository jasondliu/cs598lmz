fn = lambda: None
# Test fn.__code__.co_argcount:
def f(x, y, z=1, *args, **kwargs): pass
fn.__code__ = f.__code__
assert fn.__code__.co_argcount == 3
# Test fn.__code__.co_varnames:
fn.__code__ = f.__code__
assert fn.__code__.co_varnames == ('x', 'y', 'z', 'args', 'kwargs')
# Test fn.__code__.co_filename:
fn.__code__ = f.__code__
assert fn.__code__.co_filename == __file__
# Test fn.__code__.co_firstlineno:
fn.__code__ = f.__code__
assert fn.__code__.co_firstlineno == 10
# Test fn.__code__.co_lnotab:
fn.__code__ = f.__code__
assert fn.__code__.co_lnotab == b'\x00\x01\x06\x01\x06\x01\x06
