gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags)

# Test using gi.gi_frame.f_code in an expression.
is_test
