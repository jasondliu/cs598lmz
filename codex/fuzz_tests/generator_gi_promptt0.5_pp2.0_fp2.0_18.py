gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_GENERATOR)
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_GENERATOR_ALLOWED)

# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_COROUTINE)
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_ITERABLE_COROUTINE)

# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_ASYNC_GENERATOR)

# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_ASYNC_GENERATOR_ALLOWED)

# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_ASYNC_ITERABLE_COR
