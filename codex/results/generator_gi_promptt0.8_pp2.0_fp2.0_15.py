gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print("AttributeError expected")

# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    print("AttributeError expected")

# Test gi.gi_running
try:
    gi.gi_running
except AttributeError:
    pass
else:
    print("AttributeError expected")

# Test gi.__next__
try:
    gi.__next__()
except StopIteration:
    pass
else:
    print("StopIteration expected")
