gi = (i for i in ())
# Test gi.gi_code is None.
# Test gi.gi_frame is None.

# Verify that gi.gi_running is an int.
gi = (i for i in ())
try:
    gi.gi_running = 1
except TypeError:
    print("gi.gi_running must be an int")

# Verify that gi.gi_frame is None, and cannot be assigned to.
gi = (i for i in ())
if gi.gi_frame is not None:
    print("gi.gi_frame must be None")
try:
    gi.gi_frame = 1
except TypeError:
    print("gi.gi_frame must not be assignable")

# Verify that gi.gi_code is None, and cannot be assigned to.
gi = (i for i in ())
if gi.gi_code is not None:
    print("gi.gi_code must be None")
try:
    gi.gi_code = 1
except TypeError:
    print("gi.gi_code must not be assignable")

# Verify that gi.gi_
