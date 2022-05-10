gi = (i for i in ())
# Test gi.gi_code.
print(gi.gi_code)

# Test gi.gi_frame.
try:
    next(gi)
except StopIteration:
    # gi.gi_frame is None if gi_code.co_flags & CO_GENERATOR is not set.
    print(gi.gi_frame)
