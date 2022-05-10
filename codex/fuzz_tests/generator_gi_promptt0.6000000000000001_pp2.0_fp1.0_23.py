gi = (i for i in ())
# Test gi.gi_code is None.
gi.gi_code = None
# Setting gi.gi_code to a code object should raise a ValueError.
code = gi.gi_code
try:
    gi.gi_code = code
except ValueError:
    print("ValueError")

# Setting gi.gi_code to None should raise a ValueError.
try:
    gi.gi_code = None
except ValueError:
    print("ValueError")

# Setting gi.gi_code to a non-code object should raise a TypeError.
try:
    gi.gi_code = b'code'
except TypeError:
    print("TypeError")

# Test gi.gi_frame is None.
gi.gi_frame = None
# Setting gi.gi_frame to a frame object should raise a ValueError.
frame = gi.gi_frame
try:
    gi.gi_frame = frame
except ValueError:
    print("ValueError")

# Setting gi.gi_frame to None should raise a ValueError.
try:
    g
