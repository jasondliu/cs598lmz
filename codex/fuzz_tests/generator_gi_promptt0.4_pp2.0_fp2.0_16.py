gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_COROUTINE)

# Test gi.gi_frame.f_code.co_flags
print(gi.gi_frame.f_code.co_flags & inspect.CO_COROUTINE)

print(gi.gi_frame.f_code.co_flags & inspect.CO_FUTURE_GENERATOR_STOP)

# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_FUTURE_GENERATOR_STOP)

# Test gi.gi_frame.f_code.co_flags
print(gi.gi_frame.f_code.co_flags & inspect.CO_FUTURE_GENERATOR_STOP)

# Test gi.gi_frame.f_code.co_flags
print(gi.gi_frame.f_code.co_flags & inspect.CO_FUTURE_GENERATOR_STOP)

# Test gi.gi_frame.f
