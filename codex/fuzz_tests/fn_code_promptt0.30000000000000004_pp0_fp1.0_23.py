fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = (1, 2, 3)

# Test fn.__code__.co_argcount
try:
    fn.__code__.co_argcount = "not an int"
except TypeError:
    print("TypeError")

# Test fn.__code__.co_cellvars
try:
    fn.__code__.co_cellvars = "not a tuple"
except TypeError:
    print("TypeError")

# Test fn.__code__.co_freevars
try:
    fn.__code__.co_freevars = "not a tuple"
except TypeError:
    print("TypeError")

# Test fn.__code__.co_stacksize
try:
    fn.__code__.co_stacksize = "not an int"
except TypeError:
    print("TypeError")

# Test fn.__code__.co_flags
try:
    fn.__code__.co_flags = "not an int"
except
