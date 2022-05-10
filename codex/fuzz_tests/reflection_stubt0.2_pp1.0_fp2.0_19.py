fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the exception is raised if the code object is not a code object
# or a generator.
try:
    fn.__code__ = None
except TypeError:
    pass
else:
    raise Exception("TypeError not raised")

try:
    fn.__code__ = "not a code object"
except TypeError:
    pass
else:
    raise Exception("TypeError not raised")

# Test that the exception is raised if the code object is a code object, but
# not a generator.
def fn2():
    pass
fn.__code__ = fn2.__code__
try:
    fn()
except TypeError:
    pass
else:
    raise Exception("TypeError not raised")

# Test that the exception is raised if the code object is a generator, but
# not a generator function.
def fn3():
    yield 1
fn.__code__ = fn3().gi_code
try:
    fn()
except TypeError:
    pass
else:
    raise Exception("TypeError not raised")

# Test that
