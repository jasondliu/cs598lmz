fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# test_unpack_sequence_error
def f():
    return 1, 2, 3, 4, 5

try:
    a, b, c, d, e, f = f()
except ValueError:
    pass
else:
    raise RuntimeError

# test_unpack_sequence_error_2
def f():
    return 1, 2, 3, 4, 5

try:
    a, b, c, d, e, f, g = f()
except ValueError:
    pass
else:
    raise RuntimeError

# test_unpack_sequence_error_3
def f():
    return 1, 2, 3, 4, 5

try:
    a, b, c, d, e, f, g, h = f()
except ValueError:
    pass
else:
    raise RuntimeError

# test_unpack_sequence_error_4
def f():
    return 1, 2, 3, 4, 5

try:
    a, b, c, d, e, f,
