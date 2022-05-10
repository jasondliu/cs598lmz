gi = (i for i in ())
# Test gi.gi_code
assert gi.gi_code is None
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    assert False, "should have raised"
# Test gi.gi_running
assert gi.gi_running is None
# Test gi.gi_yieldfrom
assert gi.gi_yieldfrom is None
# test gi.gi_weakreflist
assert gi.gi_weakreflist is None
# test gi.gi_frame.f_lasti
assert gi.gi_frame.f_lasti == -1

# test gi.__next__()
try:
    gi.__next__()
except StopIteration:
    pass
else:
    assert False, "should have raised"

# test gi.send(None)
try:
    gi.send(None)
except StopIteration:
    pass
else:
    assert False, "should have raised"

# test gi.throw()
try:
    gi.throw()
except StopIteration:
