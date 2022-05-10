gi = (i for i in ())
# Test gi.gi_code
#print gi.gi_code
# Verify that gi isn't a valid iterator
try:
    next(gi)
except StopIteration:
    pass
else:
    print "next(gi) didn't raise StopIteration"
# Verify that gi.gi_frame isn't a valid frame
try:
    dis.dis(gi.gi_frame)
except ValueError:
    pass
else:
    print "dis(gi.gi_frame) didn't raise ValueError"
# Verify that gi.gi_running is false
print gi.gi_running
# Verify that gi.gi_frame doesn't have a back reference to gi
print gi.gi_frame.f_back is None
# Verify that gi.gi_frame.f_trace is None
print gi.gi_frame.f_trace is None
def func():
    pass
def func2():
    pass
# Verify that func has no trace function
print func.__code__.co_tracefunc is None
# Verify that func.__closure__ is None
print func.__closure__ is
