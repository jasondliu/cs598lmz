gi = (i for i in ())
# Test gi.gi_code:
assert next(gi).gi_code is gi.gi_code

# The "code" object of a generator is actually a built-in wrapper.  This test
# checks that the 'gi_code' field of the generator is properly updated when
# the 'gi_code' field of the built-in wrapper changes.
def f():
    for i in range(10):
        yield i

gi = iter(f())
assert next(gi) == 0
f.__code__ = ()
assert next(gi) == 1

# Test that frame.clear() clears the frame of a generator in the same way
# that frame.__init__() does.  The only difference is that clear() doesn't call
# _PyEval_EvalFrameDefault() to load the constants and cellvars.
def f():
    yield

gi = f()
frame = gi.gi_frame
frame.f_locals['x'] = 42
assert 'x' in gi.gi_frame.f_locals
frame.clear()
assert 'x' not in gi.gi_frame.
