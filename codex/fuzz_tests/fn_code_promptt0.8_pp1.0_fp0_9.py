fn = lambda: None
# Test fn.__code__ attribute
try:
    fn.__code__
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test fn.__code__.co_name attribute
try:
    fn.__code__.co_name
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test fn.__code__.co_filename attribute
try:
    fn.__code__.co_filename
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test fn.__code__.co_argcount attribute
try:
    fn.__code__.co_argcount
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test fn.__code__.co_code attribute
try:
    fn.__code__.co_code
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test fn.__code__.co_consts attribute
try:
    fn.__code__.co_consts
except AttributeError:
    print('
