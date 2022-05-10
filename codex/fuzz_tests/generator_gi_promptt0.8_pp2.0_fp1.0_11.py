gi = (i for i in ())
# Test gi.gi_code is an actual code object instead of an integer,
# as it would be e.g. with 'def gi(): yield i'
# This is only an issue on Python < 3.3.
assert isinstance(gi.gi_code, types.CodeType)
# Test gi_frame is None
assert gi.gi_frame is None
# Test gi_running is false
assert not gi.gi_running
try:
    gi.gi_running = True
except ValueError:
    pass
# Test gi_yieldfrom is None
assert gi.gi_yieldfrom is None
try:
    gi.gi_yieldfrom = True
except ValueError:
    pass
# Test gi_running is false again
assert not gi.gi_running
# Test that other attributes raise AttributeError
try:
    gi.gi_frame = True
except AttributeError:
    pass
try:
    gi.gi_code = True
except AttributeError:
    pass
try:
    gi.gi_running = True
except AttributeError:
