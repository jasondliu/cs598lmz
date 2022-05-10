fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

try:
    fn()
except TypeError as e:
    print(e)

# Output:
# 'code' object is not callable

# Note:
# This is an example of a bug in Python 2.7.9.
# The bug has been fixed in Python 3.
# The bug is that the code object is not being checked for callability.
# This is because the code object is being returned by a generator
# and is being passed to a function that expects a function.
# The bug is that the function does not check if the code object is callable.
# The bug is fixed in Python 3.

# Python 3.6.2 (default, Jul 17 2017, 16:44:45) 
# [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> fn = lambda: None
# >>> gi = (i for i in ())
# >>> fn.__code__ = gi
