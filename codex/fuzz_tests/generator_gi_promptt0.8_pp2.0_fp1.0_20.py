gi = (i for i in ())
# Test gi.gi_code
gi = (i for i in ())
assert gi.gi_code.co_argcount == 0
assert gi.gi_code.co_firstlineno == 1
gi = (i for i in ())
assert gi.gi_code.co_consts[0] == ()
assert gi.gi_code.co_consts[1] == 0
gi = (i for i in ())
# Test gi.gi_frame
gi = (i for i in ())
assert gi.gi_frame.f_lineno == 1
gi = (i for i in ())
# Test gi.gi_running
gi = (i for i in ())
assert gi.gi_running is False
assert next(gi) == 0
assert gi.gi_running is True
assert next(gi, None) is None
assert gi.gi_running is False
# Test that gi is always empty
gi = (i for i in ())
for i in range(10):
    assert next(gi, None) is None
# Test that gi is always empty
gi = (i for i
