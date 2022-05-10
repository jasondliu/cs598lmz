fn = lambda: None
# Test fn.__code__.co_argcount returns 0
print(fn.__code__.co_argcount)

# Test fn.__code__.co_consts
fn = lambda: None
fn.__code__.co_consts = (None, 1, 'hello')
print(fn.__code__.co_consts)

# Test fn.__code__.co_varnames:
fn = lambda a, b: None
print(fn.__code__.co_varnames)

# Test fn.__code__.co_argcount:
fn = lambda a, b=1, c=2, d=3, e=4, f=5, g=6, h=7: None
print(fn.__code__.co_argcount)

# Test fn.__code__.co_stacksize
# Note that this is also tested under "Test fn.__code__.co_flags"
fn = lambda a, b: None
print(fn.__code__.co_stacksize)

# Test fn.__code__.co_flags
fn =
