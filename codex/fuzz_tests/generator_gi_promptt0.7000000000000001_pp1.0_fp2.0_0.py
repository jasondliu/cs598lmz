gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags)

# Test gi.gi_frame.f_code.co_flags
print(gi.gi_frame.f_code.co_flags)

# Test gi.gi_frame.f_code.co_name
print(gi.gi_frame.f_code.co_name)
# Test gi.gi_yieldfrom
gi.gi_yieldfrom = None
gi.gi_yieldfrom = 'hello'
gi.gi_yieldfrom = 5
gi.gi_yieldfrom = object()

# Test gi_frame.f_lasti
gi.gi_frame.f_lasti = 5
gi.gi_frame.f_lasti = 'hello'
gi.gi_frame.f_lasti = object()

# Test gi_frame.f_lineno
gi.gi_frame.f_lineno = 5
gi.gi_frame.f_lineno = 'hello'
gi.gi_frame.f_lineno = object()

# Test
