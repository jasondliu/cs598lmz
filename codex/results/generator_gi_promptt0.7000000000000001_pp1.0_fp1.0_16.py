gi = (i for i in ())
# Test gi.gi_code = None
try:
    gi.gi_code = None
except TypeError:
    pass
else:
    print("TypeError not raised")
# Test gi.gi_frame = None
try:
    gi.gi_frame = None
except TypeError:
    pass
else:
    print("TypeError not raised")
# Test gi.gi_running = None
try:
    gi.gi_running = None
except TypeError:
    pass
else:
    print("TypeError not raised")
