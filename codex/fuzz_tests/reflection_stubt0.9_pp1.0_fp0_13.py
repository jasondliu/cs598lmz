fn = lambda: None
gi = (i for i in ())
fn.__code__ = c

# This sets fn.__code__.co_varnames to an empty tuple.
fn()

# Let's try delete __code__
del fn.__code__
print(fn.__code__)
# This sets fn.__code__ to None, but leaves fn.__code__.co_varnames as it is.
try:
    fn()
except AttributeError:
    print("fn.__code__ is None")
del fn
print(c.co_varnames)

# Now, let's try the same with a different c...
c = type(gi).send.__code__
fn = lambda: None
gi = (i for i in ())
fn.__code__ = c

# This sets fn.__code__.co_varnames to an empty tuple.
fn()

# Let's try delete __code__
del fn.__code__
print(fn.__code__)
# This sets fn.__code__ to None, but leaves fn.__code__.co_varnames as it is.
try:
    fn()
