gi = (i for i in ())
# Test gi.gi_code is None
gi.gi_code

# Test gi.gi_frame is None
gi.gi_frame

# Test gi.gi_running is False
gi.gi_running

# Test gi.gi_frame.f_lasti is -1
gi.gi_frame.f_lasti

import test.support

# Test gi.gi_frame.f_code.co_filename is '<string>'
gi.gi_frame.f_code.co_filename

# Test gi.gi_frame.f_code.co_firstlineno is 1
gi.gi_frame.f_code.co_firstlineno

# Test gi.gi_frame.f_code.co_name is '<genexpr>'
gi.gi_frame.f_code.co_name

# Test gi.gi_frame.f_code.co_argcount is 1
gi.gi_frame.f_code.co_argcount
gi.gi_frame.f_code.co_nlocals
gi.gi_frame.f_
