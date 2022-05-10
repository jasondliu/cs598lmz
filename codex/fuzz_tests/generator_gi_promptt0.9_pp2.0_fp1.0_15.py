gi = (i for i in ())
# Test gi.gi_code.co_name
for _ in range(1000):
	gi.gi_frame.f_code.co_name
	gi.gi_code.co_firstlineno
	gi.gi_frame.f_code.co_filename
	gi.gi_code.co_lnotab

gi.gi_frame.f_code.co_name = "foo"
gi.gi_code.co_firstlineno = 10
gi.gi_frame.f_code.co_filename = "foo.py"
gi.gi_code.co_lnotab = b'\x00\x01'

gi = (i for i in ())
# Test gi.gi_frame.f_code
for _ in range(1000):
	gi.gi_frame.f_code.co_name
	gi.gi_frame.f_code.co_firstlineno
	gi.gi_frame.f_code.co_filename
	gi.gi_frame.f_code.co_lnotab
gi.gi_frame.f_code.co_name = "foo
