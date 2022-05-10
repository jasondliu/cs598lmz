gi = (i for i in ())
# Test gi.gi_code.co_flags
print(next(gi).gi_code.co_flags)

# Test gi.gi_code.co_code
print(next(gi).gi_code.co_code)

# Test gi.gi_frame.f_code.co_name
print(next(gi).gi_frame.f_code.co_name)

# Test gi.gi_frame.f_locals
print(next(gi).gi_frame.f_locals)

# Test gi.gi_frame.f_trace
print(next(gi).gi_frame.f_trace)

# Test gi.gi_frame.f_lineno
print(next(gi).gi_frame.f_lineno)

# Test gi.gi_frame.f_lasti
print(next(gi).gi_frame.f_lasti)

# Test gi.gi_frame.f_restricted
print(next(gi).gi_frame.f_restricted)

# Test gi.gi_frame.f_builtins
print(next
