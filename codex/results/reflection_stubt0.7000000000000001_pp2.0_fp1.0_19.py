fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# noinspection PyUnresolvedReferences
def foo(x, y=None, z=None):
    return x, y, z


assert foo() == (foo, None, None)
assert foo(1) == (1, None, None)
assert foo(1, 2) == (1, 2, None)
assert foo(1, 2, 3) == (1, 2, 3)

assert foo(z=3) == (foo, None, 3)
assert foo(1, z=3) == (1, None, 3)
assert foo(z=3, y=2) == (foo, 2, 3)
assert foo(1, y=2, z=3) == (1, 2, 3)

# noinspection PyUnresolvedReferences
def foo(x, *args):
    return x, args


assert foo() == (foo, ())
assert foo(1) == (1,)
assert foo(1, 2) == (1, (2,))
assert foo(1, 2, 3) == (1, (2,
