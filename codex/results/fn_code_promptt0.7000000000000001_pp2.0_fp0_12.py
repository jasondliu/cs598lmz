fn = lambda: None
# Test fn.__code__ is what we expect it to be.
print(fn.__code__)
# <code object <lambda> at 0x1048f99b0, file "<stdin>", line 1>
# Change it to something different
fn.__code__ = 42

fn()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: <lambda>() takes 0 positional arguments but 1 was given

# We now have a function that takes 1 argument, but will always raise an exception.
fn = lambda: None
fn(42)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: <lambda>() takes 0 positional arguments but 1 was given

# Here's a little hack for creating a function that always returns a value
# (other than None).
fn = lambda: None
fn.__code__ = ( lambda x: x ).__code__.replace(co_argcount=0)

fn()
# 42

# The above is hacky, but it works
