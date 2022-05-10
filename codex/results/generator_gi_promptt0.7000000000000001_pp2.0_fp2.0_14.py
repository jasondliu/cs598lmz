gi = (i for i in ())
# Test gi.gi_code.co_flags
try:
	gi.gi_code.co_flags
except AttributeError:
	pass
else:
	print("FAIL: gi.gi_code.co_flags should not exist")

gi = (i for i in range(3))
gi.gi_code.co_flags
gi.gi_code.co_flags & CO_COROUTINE

gi = (i for i in ())
try:
	gi.gi_frame
except ValueError:
	pass
else:
	print("FAIL: gi.gi_frame should raise ValueError")

gi = (i for i in range(3))
gi.gi_frame
gi.gi_frame.f_lasti
gi.gi_frame.f_code.co_name
gi.gi_frame.f_code.co_filename
gi.gi_frame.f_code.co_nlocals
gi.gi_frame.f_code.co_firstlineno
gi.gi_frame.f_code.co_flags
gi.gi_frame.f_code.co
