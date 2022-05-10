gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags)
# Test gi.gi_code.co_code
print(bytes(gi.gi_code.co_code))
