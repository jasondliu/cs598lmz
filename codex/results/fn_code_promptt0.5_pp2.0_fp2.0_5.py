fn = lambda: None
# Test fn.__code__
try:
    fn.__code__
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test fn.__code__.co_code
try:
    fn.__code__.co_code
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test fn.__code__.co_code.__len__
try:
    fn.__code__.co_code.__len__
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test fn.__code__.co_code.__getitem__
try:
    fn.__code__.co_code.__getitem__
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test fn.__code__.co_code.__iter__
try:
    fn.__code__.co_code.__iter__
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test fn.__code__.co_code.__repr__
try:
