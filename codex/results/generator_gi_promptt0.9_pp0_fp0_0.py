gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame
assert gi and gi.gi_code and gi.gi_frame

def f():
    yield 1
def nf():
    pass

assert next(f()) == 1
try:
    next(nf())
except TypeError:
    pass
else:
    raise AssertionError

# next can raise StopIteration
assert raises(StopIteration, next, count(10)) == StopIteration(10, )

# next can raise ValueError
assert raises(ValueError, next, count())
assert raises(ValueError, next, [])

# next can raise StopIteration when given an empty iterator
assert raises(StopIteration, next, iter(())) == StopIteration()

# next can raise AttributeError when given a non-iterator
try:
    next(42)
except AttributeError as e:
    assert str(e) == "'int' object is not an iterator"
else:
    raise AssertionError

assert raises(TypeError, next, 0, True)

assert next(count(1),
