fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #20897: test that a generator function can be called with
# keyword arguments
def gen_fn(a, b, c):
    yield a
    yield b
    yield c

g = gen_fn(1, 2, 3)
assert next(g) == 1
assert next(g) == 2
assert next(g) == 3

g = gen_fn(c=3, b=2, a=1)
assert next(g) == 1
assert next(g) == 2
assert next(g) == 3

# Issue #20897: test that a generator function can be called with
# keyword arguments, even if the keyword arguments are not in the
# same order as the parameters
def gen_fn(a, b, c):
    yield a
    yield b
    yield c

g = gen_fn(c=3, a=1, b=2)
assert next(g) == 1
assert next(g) == 2
assert next(g) == 3

# Issue #20897: test that a generator function can
