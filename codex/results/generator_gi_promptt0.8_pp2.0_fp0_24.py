gi = (i for i in ())
# Test gi.gi_code.co_argcount
assert isinstance(gi.gi_code.co_argcount, int)
# Test gi.gi_frame
assert isinstance(gi.gi_frame, types.FrameType)
# Test gi_running
assert (yield from gi) is None
assert gi.gi_running
# Test gi_frame.f_code.co_name
try:
    raise StopIteration
except StopIteration:
    gi_frame = sys.exc_info()[2].tb_frame
assert 'StopIteration' == gi_frame.f_code.co_name
# Test gi.gi_frame.f_lasti
assert gi_frame.f_lasti == -1
# Test gi_frame.f_lineno
assert gi_frame.f_lineno == 10
# Test gi_frame.f_locals
assert gi_frame.f_locals == {"gi": gi}
# Test gi.gi_frame.f_code.co_filename
assert isinstance(gi_frame.f_
