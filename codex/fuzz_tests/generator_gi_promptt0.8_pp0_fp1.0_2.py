gi = (i for i in ())
# Test gi.gi_code.co_flags is CO_ITERABLE_COROUTINE
assert gi.gi_code.co_flags & 0x2000 == 0x2000
# Test gi.gi_frame.f_lasti is -1
assert gi.gi_frame.f_lasti == -1
