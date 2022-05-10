fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = (1, 2, 3)
try:
    fn.__code__.co_varnames = (1, 2, 3, 4)
except TypeError:
    print("TypeError")

# Test fn.__code__.co_argcount
print(fn.__code__.co_argcount)

# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = (1, 2, 3)
try:
    fn.__code__.co_cellvars = (1, 2, 3, 4)
except TypeError:
    print("TypeError")

# Test fn.__code__.co_freevars
fn.__code__.co_freevars = (1, 2, 3)
try:
    fn.__code__.co_freevars = (1, 2, 3, 4)
except TypeError:
    print("TypeError")

# Test fn.__code__.co_flags
print(fn
