gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_GENERATOR)
print(gi.gi_code.co_flags & inspect.CO_ITERABLE_COROUTINE)
print(gi.gi_code.co_flags & inspect.CO_ASYNC_GENERATOR)

# Test gi.gi_frame.f_code.co_flags
print(gi.gi_frame.f_code.co_flags & inspect.CO_GENERATOR)
print(gi.gi_frame.f_code.co_flags & inspect.CO_ITERABLE_COROUTINE)
print(gi.gi_frame.f_code.co_flags & inspect.CO_ASYNC_GENERATOR)

# Test gi.gi_frame.f_back.f_code.co_flags
print(gi.gi_frame.f_back.f_code.co_flags & inspect.CO_GENERATOR)
print(gi.gi_frame.f_back.f_code.co_flags & inspect.CO_ITERABLE_COR
