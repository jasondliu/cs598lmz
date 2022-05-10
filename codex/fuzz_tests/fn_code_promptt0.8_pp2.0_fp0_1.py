fn = lambda: None
# Test fn.__code__
print(fn.__code__)
print(fn.__code__.co_code)
print(fn.__code__.co_varnames)
print(fn.__code__.co_argcount)
# If a parameter has a default value, the corresponding argument is jumped over
print(fn.__defaults__)


import dis
# dis.dis(fn)


# Test fn.__globals__
print(dir(fn.__globals__))

# Test fn.__kwdefaults__
print(fn.__kwdefaults__)


def fn(x, y=1, *args, **kwargs):
    print(x, y, args, kwargs)


# Named parameter, default parameter, variable parameter, keyword parameter and
# default keyword parameter
fn(1, 2, 3, 4, a=1)
fn(1, 2, 3, a=1)
fn(x=1, y=2, a=1)
fn(1, 2, a=1)
fn(1, a=1)
fn(1)
