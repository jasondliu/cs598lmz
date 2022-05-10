gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags)
# Test gi.gi_frame.f_code.co_flags
print(gi.gi_frame.f_code.co_flags)
# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)
# Test gi.gi_frame.f_trace
def tracer(frame, event, arg):
    print(frame.f_code.co_name)

gi.gi_frame.f_trace = tracer
# Test gi.gi_frame.f_trace_opcodes
gi.gi_frame.f_trace_opcodes = True
# Test gi.gi_frame.clear_trace
gi.gi_frame.clear_trace()
# Test gi.gi_frame.f_locals
gi.gi_frame.f_locals
# Test gi.gi_frame.f_locals.update
gi.gi_frame.f_locals.update({'foo': 'bar'})
# Test gi.gi
