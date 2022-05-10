fn = lambda: None
# Test fn.__code__
print(fn.__code__)
# Test fn.__code__.co_filename
print(fn.__code__.co_filename)
# Test fn.__code__.co_name
print(fn.__code__.co_name)
# Test fn.__code__.co_firstlineno
print(fn.__code__.co_firstlineno)
# Test fn.__code__.co_argcount
print(fn.__code__.co_argcount)
# Test fn.__code__.co_varnames
print(fn.__code__.co_varnames)

# Get the code object associated with a function
def test(a, b, c):
    pass

# Test test.__code__
print(test.__code__)
# Test test.__code__.co_filename
print(test.__code__.co_filename)
# Test test.__code__.co_name
print(test.__code__.co_name)
# Test test.__code__.co_firstlineno
print(test.
