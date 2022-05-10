fn = lambda: None
# Test fn.__code__
try:
    fn.__code__
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test fn.__code__.__annotations__
try:
    fn.__code__.__annotations__
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test fn.__code__.__annotations__.items()
try:
    fn.__code__.__annotations__.items()
except AttributeError:
    print('SKIP')
    raise SystemExit

print(type(fn.__code__.__annotations__.items()))
print(list(fn.__code__.__annotations__.items()))
