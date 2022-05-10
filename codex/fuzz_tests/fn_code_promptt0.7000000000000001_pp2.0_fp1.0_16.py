fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = [1, 2, 3]
# Test fn.__code__.co_name
fn.__code__.co_name = 1

# Test fn.__code__.co_flags
fn.__code__.co_flags = 200

# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize = 200

# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno = 200
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab = "hello"

# Test fn.__code__.co_freevars
fn.__code__.co_freevars = "hello"

# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = "hello"

print("Done")
