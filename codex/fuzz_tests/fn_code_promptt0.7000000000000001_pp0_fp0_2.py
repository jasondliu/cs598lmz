fn = lambda: None
# Test fn.__code__
try:
    print(fn.__code__)
except AttributeError:
    print(0)


# Test fn.__code__.__class__
try:
    print(fn.__code__.__class__)
except AttributeError:
    print(0)


# Test fn.__code__.co_filename
try:
    print(fn.__code__.co_filename)
except AttributeError:
    print(0)


# Test fn.__code__.co_name
try:
    print(fn.__code__.co_name)
except AttributeError:
    print(0)


# Test fn.__code__.co_nlocals
try:
    print(fn.__code__.co_nlocals)
except AttributeError:
    print(0)


# Test fn.__code__.co_varnames
try:
    print(fn.__code__.co_varnames)
except AttributeError:
    print(0)


# Test fn.__code__.co_
