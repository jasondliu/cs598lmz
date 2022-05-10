fn = lambda: None
# Test fn.__code__ with no arguments.
fn.__code__
# Test fn.__code__ with a single argument.
fn.__code__(0)
# Test fn.__code__ with a tuple containing one argument.
fn.__code__((0,))
# Test fn.__code__ with a tuple containing three arguments.
fn.__code__((0, 1, 2))
# Test fn.__code__ with a tuple containing too few arguments.
try:
    fn.__code__(())
except TypeError:
    pass
else:
    raise Exception('TypeError expected')
# Test fn.__code__ with a tuple containing too many arguments.
try:
    fn.__code__((0, 1, 2, 3))
except TypeError:
    pass
else:
    raise Exception('TypeError expected')
# Test fn.__code__ with a dict containing one argument.
fn.__code__({'x': 0})
# Test fn.__code__ with a dict containing three arguments.
fn.__code__({'x': 0, 'y': 1, 'z': 2})
# Test
