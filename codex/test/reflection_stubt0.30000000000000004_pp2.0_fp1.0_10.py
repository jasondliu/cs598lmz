fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'test'
fn.__module__ = 'test'

# Test that the code object is not wrapped by the trace function
# and that the trace function is called with the original code object.
def trace(frame, event, arg):
    assert frame.f_code is fn.__code__
    assert frame.f_code is gi.gi_code
    return trace

