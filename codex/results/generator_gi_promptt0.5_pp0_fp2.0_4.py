gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_GENERATOR)
# Test gi.gi_frame.f_code.co_flags
print(gi.gi_frame.f_code.co_flags & inspect.CO_GENERATOR)

# Test generator-iterator.gi_code.co_flags
gi = (i for i in ()).__iter__()
print(gi.gi_code.co_flags & inspect.CO_GENERATOR)
# Test generator-iterator.gi_frame.f_code.co_flags
print(gi.gi_frame.f_code.co_flags & inspect.CO_GENERATOR)
