fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'irrelevant_function'

# Make sure the repr does not recurse indefinitely
print(repr(gi))

# Issue #11152: Make sure frame.clear() does not clear the frame
# locals for other frames referencing the same frame object.

def capture_locals(func, *args, **kwds):
    def func_wrapper():
        return func(*args, **kwds)
    return func_wrapper.__closure__[0].cell_contents

def f():
    x = 42
    y = capture_locals(f)
    return y

d = f()
print('%r should contain x: %r' % (d, 'x' in d))
