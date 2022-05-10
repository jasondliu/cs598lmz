gi = (i for i in ())
# Test gi.gi_code if it's set
assert gi.gi_code is None
assert gi.gi_frame is not None
assert gi.gi_frame.f_code is None
# Test f.f_code if it's set
assert gi.gi_frame.f_code is None
# Test the actual iterator object
assert list(gi) == []

def f():
    yield 42

assert isinstance(f(), types.GeneratorType)
def g():
    x = 0
    while True:
        x += 1
        yield x

gi = g()

# Test to make sure a failing StopIteration is handled properly
# for genexprs.
def f(x):
    return (i for i in x)
try:
    next(f(g()))
    assert False
except StopIteration as e:
    # Check the error message.
    assert str(e) == "generator exhausted"

assert 'An_instancemethod' in dir(f)
assert '__name__' in dir(f)
assert '__self__' in dir(f.__call
