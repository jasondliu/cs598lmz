gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
gi.gi_code == None
gi.gi_code.__class__

# Test gi.gi_frame
gi.gi_frame == None

# Test gi.gi_running
gi.gi_running == 0

# Test gi.gi_yieldfrom
gi.gi_yieldfrom == None

# Test gi.gi_yieldfrom.__qualname__
try:
    gi.gi_yieldfrom.__qualname__
except AttributeError:
    print("AttributeError")
