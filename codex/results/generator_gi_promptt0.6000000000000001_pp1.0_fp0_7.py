gi = (i for i in ())
# Test gi.gi_code
print gi.gi_code
# Test gi.gi_frame
print gi.gi_frame
# Test gi.gi_running
print gi.gi_running
# Test gi.gi_yieldfrom
print gi.gi_yieldfrom

# Test gi.send(value)
print gi.send(None)
# Test gi.throw(type, value=None, traceback=None)
gi.throw(Exception)
# Test gi.close()
gi.close()

# Test gi.gi_frame.f_lasti
print gi.gi_frame.f_lasti
# Test gi.gi_frame.f_trace
print gi.gi_frame.f_trace

# Test gi.gi_frame.f_back
print gi.gi_frame.f_back
# Test gi.gi_frame.f_code
print gi.gi_frame.f_code
# Test gi.gi_frame.f_exc_traceback
print gi.gi_frame.f_exc_
