gi = (i for i in ())
# Test gi.gi_code.co_filename and gi.gi_frame.f_code.co_filename
try:
    i = next(gi)
except StopIteration:
    pass

i = 0
try:
    i = next(gi)
except StopIteration:
    pass

# Test gi_frame.f_locals["__class__"] is None

# Test invalid 'yield from' statements
def f():
    def g():
        yield from 0
    yield from g()
try:
    next(f())
except TypeError:
    pass

def g():
    yield from (i for i in ())[0]
try:
    next(g())
except TypeError:
    pass

# 'yield from' statement in function which return None
def with_return(x):
    yield from (i for i in range(x))
    return

def without_return(x):
    yield from (i for i in range(x))

# 'yield from' statement in function which return generator
def two_yield_from(x):
    yield
