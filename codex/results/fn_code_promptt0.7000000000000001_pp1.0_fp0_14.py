fn = lambda: None
# Test fn.__code__.co_name
fn.__code__.co_name

# Test fn.__code__.co_firstlineno
# and fn.__code__.co_lnotab
def fn(): pass
fn.__code__.co_firstlineno
fn.__code__.co_lnotab

# Test fn.__code__.co_varnames
def fn():
    x = 1
fn.__code__.co_varnames
