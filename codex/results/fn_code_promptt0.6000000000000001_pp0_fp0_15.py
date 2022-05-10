fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = (1, 2, 3)
try:
    fn.__code__.co_varnames = "a"
except TypeError:
    print("TypeError")

# Test fn.__code__.co_argcount
try:
    fn.__code__.co_argcount = "a"
except TypeError:
    print("TypeError")

# Test fn.__code__.co_flags
fn.__code__.co_flags = 1
try:
    fn.__code__.co_flags = "a"
except TypeError:
    print("TypeError")

# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = (1, 2, 3)
try:
    fn.__code__.co_cellvars = "a"
except TypeError:
    print("TypeError")

# Test fn.__code__.co_freevars
fn.__code__.co_freevars = (1
