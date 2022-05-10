gi = (i for i in ())
# Test gi.gi_code is not None.
try:
    next(gi)
except StopIteration:
    pass
else:
    raise RuntimeError("'gi.gi_code is not None' failed")

# Test gi.gi_frame is not None.
try:
    next(gi)
except StopIteration:
    pass
else:
    raise RuntimeError("'gi.gi_frame is not None' failed")

# Test gi.gi_running, gi.gi_yieldfrom, gi.gi_frame.f_lasti and gi.gi_frame.f_lineno
def f(gi):
    _, _, _, gi.gi_running, gi.gi_yieldfrom, gi.gi_frame.f_lasti, gi.gi_frame.f_lineno = yield from 1

def g():
    gi = f(gi_holder)
    gi_holder.gi_running = gi.gi_running
    gi_holder.gi_yieldfrom = gi.gi_yieldfrom
    gi_
