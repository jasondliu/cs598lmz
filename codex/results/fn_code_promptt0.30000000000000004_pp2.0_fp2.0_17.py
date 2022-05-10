fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = (1, 2, 3)
try:
    fn.__code__.co_varnames = (1, 2, 3)
except TypeError:
    print('TypeError')

# Test fn.__code__.co_argcount
print(fn.__code__.co_argcount)
try:
    fn.__code__.co_argcount = 1
except TypeError:
    print('TypeError')

# Test fn.__code__.co_argcount
print(fn.__code__.co_argcount)
try:
    fn.__code__.co_argcount = 1
except TypeError:
    print('TypeError')

# Test fn.__code__.co_flags
print(fn.__code__.co_flags)
try:
    fn.__code__.co_flags = 1
except TypeError:
    print('TypeError')

# Test fn.__code__.co_code
print(fn.__code__.co_code
