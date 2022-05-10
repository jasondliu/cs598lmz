fn = lambda: None
# Test fn.__code__.co_varnames
def foo(a, b, c=1, d=2, e=3):
    pass
# Test fn.__code__.co_names
# Test fn.__code__.co_consts
def bar(a, b, c=1, d=2, e=3):
    pass
# Test fn.__code__.co_flags
def baz(a, b, c=1, d=2, e=3):
    pass

# Test fn.__code__.co_argcount
def qux(a, b, c=1, d=2, e=3):
    pass

# Test fn.__code__.co_argcount
def quux(a, b, *args, c=1, d=2, e=3, **kwargs):
    pass

# Test fn.__code__.co_argcount
def corge(a, b, c=1, d=2, e=3, *args, **kwargs):
    pass

# Test fn.__code__.co_argcount
