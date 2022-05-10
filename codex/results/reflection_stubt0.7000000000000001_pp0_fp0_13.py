fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__()

# calling a generator object with an argument
# should not be allowed since it's not a function
# (i.e. not a callable object)
try:
    gi(1)
except TypeError as e:
    print(e)

# calling a generator should work
gi = (i for i in ())
gi()

# calling a generator should also work
gi = (i for i in ())
gi.__code__()

# calling a generator object with an argument
# should not be allowed since it's not a function
# (i.e. not a callable object)
try:
    gi.__code__(1)
except TypeError as e:
    print(e)


# calling a generator object with an argument
# should not be allowed since it's not a function
# (i.e. not a callable object)
try:
    gi.__code__(1)
except TypeError as e:
    print(e)

# calling a generator object with an argument
# should not be allowed since it's
