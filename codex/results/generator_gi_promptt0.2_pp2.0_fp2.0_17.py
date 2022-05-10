gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags)

# Test gi.gi_frame.f_code.co_flags
print(gi.gi_frame.f_code.co_flags)

# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)

# Test gi.gi_frame.f_locals
print(gi.gi_frame.f_locals)

# Test gi.gi_frame.f_trace
print(gi.gi_frame.f_trace)

# Test gi.gi_running
print(gi.gi_running)

# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)

# Test gi.send(None)
print(gi.send(None))

# Test gi.throw(StopIteration)
try:
    gi.throw(StopIteration)
except StopIteration:
    print("StopIteration")

# Test gi.close()
gi.close()

