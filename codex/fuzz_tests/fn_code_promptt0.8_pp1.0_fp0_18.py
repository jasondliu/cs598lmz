fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = None
# Test fn.__code__.co_filename
fn.__code__.co_filename = None
# Test fn.__code__.co_name
fn.__code__.co_name = None

# Test fn.__code__.co_flags
fn.__code__.co_flags = 0
# Test fn.__code__.co_flags
fn.__code__.co_flags = None
print(fn.__code__.co_flags)
