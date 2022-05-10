gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame
assert gi.gi_code is f.__code__
assert gi.gi_frame is f.__code__.co_firstlineno
