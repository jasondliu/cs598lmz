fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__ = type('code', (object,), {'co_varnames': ('a', 'b', 'c')})
print(fn.__code__.co_varnames)

# Test fn.__code__.co_argcount
fn.__code__ = type('code', (object,), {'co_argcount': 1})
print(fn.__code__.co_argcount)

# Test fn.__code__.co_flags
fn.__code__ = type('code', (object,), {'co_flags': inspect.CO_VARARGS})
print(fn.__code__.co_flags & inspect.CO_VARARGS)

# Test fn.__code__.co_argcount
fn.__code__ = type('code', (object,), {'co_argcount': -1})
try:
    fn.__code__.co_argcount
except ValueError as e:
    print(e)

# Test inspect.ismethod(fn)
class Foo(object
