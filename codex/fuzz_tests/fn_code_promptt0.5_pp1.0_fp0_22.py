fn = lambda: None
# Test fn.__code__.co_argcount
try:
    fn.__code__.co_argcount
except AttributeError:
    pass
else:
    print('FAILED: fn.__code__.co_argcount')

# Test fn.__code__.co_cellvars
try:
    fn.__code__.co_cellvars
except AttributeError:
    pass
else:
    print('FAILED: fn.__code__.co_cellvars')

# Test fn.__code__.co_code
try:
    fn.__code__.co_code
except AttributeError:
    pass
else:
    print('FAILED: fn.__code__.co_code')

# Test fn.__code__.co_consts
try:
    fn.__code__.co_consts
except AttributeError:
    pass
else:
    print('FAILED: fn.__code__.co_consts')

# Test fn.__code__.co_filename
try:
    fn.__code__.
