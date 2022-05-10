gi = (i for i in ())
# Test gi.gi_code here.
assert gi.gi_code is None
# Check whether gi_code is mutable.
gi.gi_code = 0
assert gi.gi_code == 0

gi = (i for i in range(0))
# Test gi.gi_code here.
assert gi.gi_code is None
# Check whether gi_code is mutable.
gi.gi_code = 0
assert gi.gi_code == 0

gi = (i for i in range(1))
# Test gi.gi_code here.
assert gi.gi_code is not None
assert gi.gi_code.co_code.startswith(b'|\x03d\x00S\x00')
assert gi.gi_frame.f_globals is globals()
# TODO find a way to test the line in .co_filename
# TODO find a way to test the line in .co_firstlineno
# gi.gi_code.co_filename & gi.gi_code.co_firstlineno
# Check whether g
