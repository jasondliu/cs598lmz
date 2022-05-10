gi = (i for i in ())
# Test gi.gi_code is None

# This is a generator-iterator.  Check that it has the right type,
# and that gi_code is not None
gi = (i for i in range(10))
# Test gi.gi_code is not None

# This is a generator-iterator.  Check that it has the right type,
# and that gi_code is not None
gi = (i for i in range(10) if i > 5)
# Test gi.gi_code is not None

# This is a generator-iterator.  Check that it has the right type,
# and that gi_code is not None
def foo():
    yield 1
    yield
    yield 1, 2, 3
gi = foo()
# Test gi.gi_code is not None

# This is a generator-iterator.  Check that it has the right type,
# and that gi_code is not None
def foo():
    for i in range(10):
        yield i
gi = foo()
# Test gi.gi_code is not None

# This is a generator-iterator.
