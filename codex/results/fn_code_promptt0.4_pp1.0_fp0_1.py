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

# Test fn.__code__.co_code[0]
try:
    fn.__code__.co_code[0]
except TypeError:
    print('SKIP')
    raise SystemExit

print(fn.__code__.co_code[0])

# Test fn.__code__.co_code[0] = 0
try:
    fn.__code__.co_code[0] = 0
except TypeError:
    print('SKIP')
    raise SystemExit

print('OK')
