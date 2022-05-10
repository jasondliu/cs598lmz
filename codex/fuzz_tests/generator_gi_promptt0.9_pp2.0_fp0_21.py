gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame
print(gi.gi_code is d.__code__, gi.gi_frame is f)

# Iterate over gi
print(next(gi))
print(next(gi))
print(next(gi))

# Raise exception explicitly
gi.throw(ZeroDivisionError)
