gi = (i for i in ())
# Test gi.gi_code is None
gi.gi_code
# Test gi.gi_frame is None
gi.gi_frame
# Test gi.gi_running
gi.gi_running
# Test gi.gi_frame.f_lasti is None
gi.gi_frame.f_lasti
# Test gi.gi_frame.f_trace is None
gi.gi_frame.f_trace
# Test gi.gi_frame.f_exc_traceback is None
gi.gi_frame.f_exc_traceback
# Test gi.gi_frame.f_exc_type is None
gi.gi_frame.f_exc_type
# Test gi.gi_frame.f_exc_value is None
gi.gi_frame.f_exc_value
# Test gi.gi_frame.f_restricted is True
gi.gi_frame.f_restricted
# Test gi.gi_frame.f_builtins is sys.modules['__builtin__'].__dict__
gi.gi_frame.f_builtins is sys.modules['__builtin__'
