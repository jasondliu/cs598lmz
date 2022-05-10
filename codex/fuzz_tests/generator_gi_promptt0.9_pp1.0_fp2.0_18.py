gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    print('AttributeError')

# Note: Bound methods/functions are defined explicitly in ISO C99
# 7.14.1.8/4.  They don't exist as distinct types in Python, and
# various things (in particular, cyclic gc with __del__) need to
# work seamlessly on them.  Consequently, this test just attempts

# functions that are bound methods in CPython should have a
# non-NULL im_self pointer, even if bound to a NULL object
def func(): pass
func.__get__(0)
print(func.__self__ is not None)
del func

# But not if they are C-functions.
print(min.__self__ is None)
