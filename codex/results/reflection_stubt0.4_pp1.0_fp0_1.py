fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    fn()
except TypeError:
    pass
else:
    raise Exception("should have raised TypeError")

# test that we don't crash if we have a generator with no code object
# (this is a corner case, but it can happen)
def g():
    yield 1
g.__code__ = None

# test that we don't crash if we have a generator with a code object
# that doesn't have a co_code attribute
def g():
    yield 1
g.__code__ = (i for i in ())

# test that we don't crash if we have a generator with a code object
# that has a co_code attribute that is not a string
def g():
    yield 1
g.__code__ = type(lambda: None)

# test that we don't crash if we have a generator with a code object
# that has a co_code attribute that is a string, but not a valid bytecode
def g():
    yield 1
g.__code__ = type(lambda: None).__code__
g.__code__.co_code =
