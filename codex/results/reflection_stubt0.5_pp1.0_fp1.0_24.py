fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(lambda: None)()
fn.__code__.co_code = b'\x00'
fn.__code__.co_flags = 0
gi.gi_frame = fn.__code__.co_frame = type(lambda: None)()
gi.gi_frame.f_lasti = -1
gi.gi_frame.f_lineno = -1
gi.gi_frame.f_trace = None
# END INITIALIZATION

# BEGIN TEST

# Make sure that the trace function is not called when the frame is not
# active.

def check_trace(frame, event, arg):
    raise AssertionError("shouldn't have traced")

sys.settrace(check_trace)

try:
    next(gi)
except StopIteration:
    pass

# END TEST
