gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & CO_GENERATOR)

# Test the presence of gi_frame
print(hasattr(gi, 'gi_frame'))

# Test the presence of gi_running
print(hasattr(gi, 'gi_running'))
