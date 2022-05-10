gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_GENERATOR)

# Test gi.gi_frame.f_code.co_flags
print(gi.gi_frame.f_code.co_flags & inspect.CO_GENERATOR)

# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)

# Test gi.gi_frame.f_lineno
print(gi.gi_frame.f_lineno)

# Test gi.gi_running
print(gi.gi_running)

# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)

# Test gi.__name__
print(gi.__name__)

# Test gi.__qualname__
print(gi.__qualname__)

# Test gi.__module__
print(gi.__module__)

# Test gi.__annotations__
print(gi.__annotations__)

# Test gi.
