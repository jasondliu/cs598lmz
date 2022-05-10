gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError, e:
    pass
else:
    raise TestFailed, "gi.gi_code should not exist"

# Test gi.gi_running
try:
    gi.gi_running
except AttributeError, e:
    pass
else:
    raise TestFailed, "gi.gi_running should not exist"

# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError, e:
    pass
else:
    raise TestFailed, "gi.gi_frame should not exist"

# Test gi.gi_frame.f_back
try:
    gi.gi_frame.f_back
except AttributeError, e:
    pass
else:
    raise TestFailed, "gi.gi_frame.f_back should not exist"

# Test gi.gi_frame.f_builtins
# Note that this works because the generator's global dict is
# the module's global dict
if gi.gi_frame.f
