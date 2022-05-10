fn = lambda: None
# Test fn.__code__.co_freevars
assert fn.__code__.co_freevars == ()

fn.__code__.co_freevars = (1,)
# Test fn.__code__.co_freevars
assert fn.__code__.co_freevars == ()

# Test fn.__code__.co_varnames
assert fn.__code__.co_varnames == ()

fn.__code__.co_varnames = (1,)
# Test fn.__code__.co_varnames
assert fn.__code__.co_varnames == ()
