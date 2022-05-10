fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__qualname__ = 'fn'

with pytest.raises(TypeError):
    fn()

# TODO: test more cases

# test __code__
def fn():
    pass

assert fn.__code__.co_filename == __file__
assert fn.__code__.co_name == 'fn'
assert fn.__code__.co_firstlineno == inspect.currentframe().f_lineno - 1

# test __defaults__
def fn(a, b=0, c=1):
    return a, b, c

assert fn.__defaults__ == (0, 1)

# test __kwdefaults__
def fn(a, b=0, c=1, *, d=2, e=3):
    return a, b, c, d, e

assert fn.__kwdefaults__ == {'d': 2, 'e': 3}

# test __annotations__
def fn(a: int, b: str, c
