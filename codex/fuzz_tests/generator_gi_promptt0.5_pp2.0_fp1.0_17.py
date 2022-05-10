gi = (i for i in ())
# Test gi.gi_code is None

gi = (i for i in ())
# Test gi.gi_frame is not None

gi = (i for i in ())
# Test gi.gi_running is False

gi = (i for i in ())
# Test gi.gi_yieldfrom is None

gi = (i for i in ())
# Test gi.gi_frame.f_lasti is -1

gi = (i for i in ())
# Test gi.gi_frame.f_lineno is 1

gi = (i for i in ())
# Test gi.gi_frame.f_code.co_name is '<genexpr>'

gi = (i for i in ())
# Test gi.gi_frame.f_code.co_varnames is ('i',)

gi = (i for i in ())
# Test gi.gi_frame.f_code.co_argcount is 0

gi = (i for i in ())
# Test gi.gi_frame.f_code.co_flags is 67

gi = (i for
