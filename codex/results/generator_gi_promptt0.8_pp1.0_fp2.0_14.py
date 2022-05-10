gi = (i for i in ())
# Test gi.gi_code returns <code> object.
assert type(gi.gi_code) is type(next.__code__)


# Issue 27882: A function with a generator for its body returns a generator.
def f():
    yield 1
    return
    yield 2
g = f()
assert isinstance(g, types.GeneratorType)
assert isinstance(g, types.FunctionType)
assert next(g) == 1
try:
    next(g)
except StopIteration as s:
    assert s.value is None
else:
    assert False, "StopIteration should have been raised"

# Issue 36109: Test type of generator yield expression types
def f_yield_val():
    yield 1
def f_yield_tuple():
    yield (1,)
def f_yield_gen():
    yield i for i in range(5)
def f_yield_str():
    yield "abc"
def f_yield_list():
    yield [1]
def f_yield_if():
    if True:
        yield 1
    else:

