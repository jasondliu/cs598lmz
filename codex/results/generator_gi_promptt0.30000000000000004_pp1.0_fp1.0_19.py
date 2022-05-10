gi = (i for i in ())
# Test gi.gi_code.co_flags
try:
    gi.gi_code.co_flags
except AttributeError:
    pass
else:
    raise RuntimeError("gi.gi_code.co_flags should not exist")

# Test gi.gi_frame.f_code.co_flags
try:
    gi.gi_frame.f_code.co_flags
except AttributeError:
    pass
else:
    raise RuntimeError("gi.gi_frame.f_code.co_flags should not exist")

# Test gi.gi_frame.f_back.f_code.co_flags
try:
    gi.gi_frame.f_back.f_code.co_flags
except AttributeError:
    pass
else:
    raise RuntimeError("gi.gi_frame.f_back.f_code.co_flags should not exist")

# Test gi.gi_frame.f_back.f_back.f_code.co_flags
try:
    gi.gi_frame.f_back.f_back.f_code
