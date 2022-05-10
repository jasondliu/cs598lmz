gi = (i for i in ())
# Test gi.gi_code.co_flags (and gi.gi_frame)
assert gi.gi_code.co_flags & (sys.CO_GENERATOR | 0x10)
# Test gi.gi_code.co_stacksize
assert gi.gi_code.co_stacksize == 0
# Test gi.gi_code.co_consts[0].co_filename
assert gi.gi_code.co_consts[0].co_filename == filename
# Test gi.gi_code.co_consts[0].co_name
assert gi.gi_code.co_consts[0].co_name == 'g'
# Test gi.gi_frame.f_lasti
assert gi.gi_frame.f_lasti == -1
# Test gi.gi_frame.f_lineno
assert gi.gi_frame.f_lineno == 2
# Test gi.gi_frame.f_code.co_filename
assert gi.gi_frame.f_code.co_filename == filename
# Test gi.gi
