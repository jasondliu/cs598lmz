gi = (i for i in ())
# Test gi.gi_code, gi.gi_frame and gi.gi_running
def f():
    yield 1
    yield 2
g = f()
assert g.gi_frame.f_lasti == -1
assert g.gi_code.co_name == 'f'
assert not g.gi_running
g.__next__()
assert g.gi_frame.f_lasti != -1
assert g.gi_code.co_name == 'f'
assert g.gi_running
g.__next__()
assert g.gi_frame.f_lasti != -1
assert g.gi_code.co_name == 'f'
assert g.gi_running
try:
    g.__next__()
except StopIteration:
    pass
assert g.gi_frame.f_lasti != -1
assert g.gi_code.co_name == 'f'
assert not g.gi_running

# gi.gi_frame should be None for gi = (i for i in ())
assert gi.gi_frame is None
assert gi.gi_code
