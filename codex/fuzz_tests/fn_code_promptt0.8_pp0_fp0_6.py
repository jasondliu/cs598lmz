fn = lambda: None
# Test fn.__code__; it should match the function
print(fn.__code__.co_filename)
print(fn.__code__.co_name)

# Test fn.__closure__; it should be non-empty
print(fn.__closure__)

# Test fn.__defaults__; it should not exist
try:
    print(fn.__defaults__)
except AttributeError as err:
    print(err)

# Test fn.__dict__; it should be empty
print(fn.__dict__)

# Test fn.__globals__; it should match the enclosing module
print(fn.__globals__ is globals())

# Test fn.__doc__; it should equal "Test fn.__code__"
print(fn.__doc__)

# The next two test attributes that may or may not exist.
# This is because they are implementation-dependent and
# may not be defined. 
# Test fn.__name__; it should match the function name
if hasattr(fn, '__name__'):
    print(fn.__
