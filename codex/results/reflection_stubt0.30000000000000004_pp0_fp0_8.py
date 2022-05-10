fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_object_attributes
def f(): pass
assert f.__code__.co_argcount == 0
assert f.__code__.co_nlocals == 0
assert f.__code__.co_stacksize == 2
assert f.__code__.co_flags == 67
assert f.__code__.co_code == b'd\x00S'
assert f.__code__.co_consts == (None,)
assert f.__code__.co_names == ()
assert f.__code__.co_varnames == ()
assert f.__code__.co_filename == __file__
assert f.__code__.co_name == 'f'
assert f.__code__.co_firstlineno == 2
assert f.__code__.co_lnotab == b'\x00\x01\x0c\x01'

def f(x, y):
    a = 1
    b = 2
    c = a + b
    return c

assert f.__code__.
