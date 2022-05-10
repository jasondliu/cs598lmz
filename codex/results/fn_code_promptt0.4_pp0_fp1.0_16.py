fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = (1, 2, 3)
# Test fn.__code__.co_varnames[0]
fn.__code__.co_varnames[0] = 1
# Test fn.__code__.co_varnames[1]
fn.__code__.co_varnames[1] = 2
# Test fn.__code__.co_varnames[2]
fn.__code__.co_varnames[2] = 3

# Test fn.__code__.co_names
fn.__code__.co_names = (1, 2, 3)
# Test fn.__code__.co_names[0]
fn.__code__.co_names[0] = 1
# Test fn.__code__.co_names[1]
fn.__code__.co_names[1] = 2
# Test fn.__code__.co_names[2]
fn.__code__.co_names[2] = 3

# Test fn.
