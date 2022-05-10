fn = lambda: None
# Test fn.__code__
try:
    fn.__code__
except AttributeError:
    pass
else:
    print('FAILED: fn.__code__')
# Test fn.__closure__
try:
    fn.__closure__
except AttributeError:
    pass
else:
    print('FAILED: fn.__closure__')
# Test fn.__defaults__
try:
    fn.__defaults__
except AttributeError:
    pass
else:
    print('FAILED: fn.__defaults__')
# Test fn.__dict__
try:
    fn.__dict__
except AttributeError:
    print('FAILED: fn.__dict__')
# Test fn.__doc__
try:
    fn.__doc__
except AttributeError:
    print('FAILED: fn.__doc__')
# Test fn.__globals__
try:
    fn.__globals__
except AttributeError:
    print('FAILED: fn.__globals__')
# Test fn.__kwdefault
