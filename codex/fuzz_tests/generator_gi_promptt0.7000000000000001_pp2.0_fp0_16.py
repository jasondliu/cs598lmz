gi = (i for i in ())
# Test gi.gi_code is not NULL.
inspect.getgeneratorinfo(gi)
# Test if a generator returns a NULL iterator.
def f():
    yield from ()
inspect.getgeneratorinfo(f())
# Test if a generator returns a NULL iterator.
def f():
    yield from None
inspect.getgeneratorinfo(f())
# Test if a generator returns a NULL iterator.
def f():
    yield from []
inspect.getgeneratorinfo(f())
# Test if a generator returns a NULL iterator.
def f():
    yield from [][:]
inspect.getgeneratorinfo(f())
# Test if a generator returns a NULL iterator.
def f():
    yield from [][:]
inspect.getgeneratorinfo(f())
# Test if a generator returns a NULL iterator.
def f():
    yield from ''.replace('', '')
inspect.getgeneratorinfo(f())
# Test if a generator returns a NULL iterator.
def f():
    yield from [][:]
inspect.getgeneratorinfo(f())
# Test if a generator returns a NULL iterator.
