fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    fn()
except TypeError:
    pass
else:
    raise RuntimeError("should have raised TypeError")

# Test that we can't set __code__ to an object that isn't a code object
# or a tuple.

try:
    fn.__code__ = 1
except TypeError:
    pass
else:
    raise RuntimeError("should have raised TypeError")

# Test that we can't set __code__ to a tuple that has the wrong size.

try:
    fn.__code__ = ()
except ValueError:
    pass
else:
    raise RuntimeError("should have raised ValueError")

# Test that we can't set __code__ to a tuple that has the wrong type for
# each element.

try:
    fn.__code__ = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                   18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
