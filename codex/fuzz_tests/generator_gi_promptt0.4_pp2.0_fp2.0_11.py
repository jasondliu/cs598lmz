gi = (i for i in ())
# Test gi.gi_code is None
# Test gi.gi_frame is None
# Test gi.gi_running is False
# Test gi.gi_yieldfrom is None
# Test gi.gi_name is ''
# Test gi.gi_qualname is ''
# Test gi.gi_frame.f_lasti is -1
# Test gi.gi_frame.f_lineno is 0
# Test gi.gi_frame.f_code is None
# Test gi.gi_frame.f_locals is {}
# Test gi.gi_frame.f_globals is {}
# Test gi.gi_frame.f_back is None
# Test gi.gi_frame.f_builtins is {}
# Test gi.gi_frame.f_restricted is False
# Test gi.gi_frame.f_trace is None

def f():
    yield 1
    yield 2
    yield 3

gi = f()
# Test gi.gi_code.co_name is 'f'
# Test gi.gi_code.co_arg
