gi = (i for i in ())
# Test gi.gi_code.co_name
assert gi.gi_code.co_name == ''
# Test gi.gi_frame.f_code.co_name
assert gi.gi_frame.f_code.co_name == ''
# Test gi.gi_running
try:
    next(gi)
except StopIteration:
    pass
assert gi.gi_running == 0
# Test gi.gi_frame.f_lasti
assert gi.gi_frame.f_lasti == -1
# Test gi.gi_frame.f_lineno
assert gi.gi_frame.f_lineno == 1

# Test gi_code.co_flags
def f():
    yield
gi = f()
assert gi.gi_code.co_flags & 0x20 != 0

# Test gi_frame.f_back
def f():
    yield
gi = f()
try:
    next(gi)
except StopIteration:
    pass
assert gi.gi_frame.f_back is None

# Test gi_frame
