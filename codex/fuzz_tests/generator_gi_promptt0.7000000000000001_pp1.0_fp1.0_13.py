gi = (i for i in ())
# Test gi.gi_code.co_firstlineno
assert gi.gi_code.co_firstlineno == 3

# Test gi.gi_frame.f_back
def f():
    g1 = (i for i in ())
    return g1
g2 = f()
g3 = g2.gi_frame.f_back.f_back
assert g3.f_code.co_name == 'f'

# Test keyword arguments to next()
def f():
    yield 0
    yield 1
    yield 2
    yield 3

g = f()

assert next(g) == 0
assert next(g, 42) == 1
assert next(g) == 2
assert next(g, 42) == 3

try:
    # This should raise an exception
    next(g)
except StopIteration:
    pass
else:
    assert False, "should raise StopIteration"

assert next(g, 42) == 42
try:
    # This should raise an exception
    next(g, 42)
except StopIteration:
    pass
else:
    assert
