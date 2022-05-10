gi = (i for i in ())
# Test gi.gi_code.co_flags.

try:
    gi.gi_code.co_flags
except AttributeError:
    print("AttributeError")
# Test gi.gi_frame.f_locals

try:
    gi.gi_frame.f_locals
except AttributeError:
    print("AttributeError")
