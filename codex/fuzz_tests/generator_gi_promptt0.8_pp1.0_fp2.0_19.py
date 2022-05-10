gi = (i for i in ())
# Test gi.gi_code == None, which should not raise an exception
print gi.gi_code
print gi.gi_frame
print gi.gi_running
