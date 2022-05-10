gi = (i for i in ())
# Test gi.gi_code 
int(gi.gi_code is None) 
int(gi.gi_frame is None) 
int(gi.gi_running is None) 
int(gi.gi_name == '') 
int(gi.gi_filename == '') 
# Test gi.gi_next
try:
    gi.gi_next
except AttributeError:
    print("passed")
else:
    raise TestFailed("gi_next should raise AttributeError")

# Test gi.gi_frame
try:
    gi.gi_frame
except ValueError:
    print("passed")
else:
    raise TestFailed("gi_frame should raise ValueError")

# Test gi.gi_running
try:
    gi.gi_running
except ValueError:
    print("passed")
else:
    raise TestFailed("gi_running should raise ValueError")

try:
    gi.gi_code = None
except AttributeError:
    print("passed")
else:
    raise TestFailed("gi_code
