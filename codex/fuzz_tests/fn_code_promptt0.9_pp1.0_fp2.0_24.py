fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__.co_argcount = property(lambda self: 1)
# Test fn.__code__.co_argcount
fn.__code__.co_nlocals = property(lambda self: 1)
# Test fn.__code__.co_argcount
fn.__code__.co_consts = property(lambda self: 0)
# Test fn.__code__.co_argcount
fn.__code__.co_names = property(lambda self: 0)
# Test fn.__code__.co_argcount
fn.__code__.co_varnames = property(lambda self: 0)
# Test fn.__code__.co_argcount
fn.__code__.co_freevars = property(lambda self: (1, 2))
# Test fn.__code__.co_flags = property(lambda self: 33)
# Test fn.co_flags = property(lambda self: 33)
# Test fn.co_flags = property(lambda self: 33)
# print(fn)
# return fn()
fn
