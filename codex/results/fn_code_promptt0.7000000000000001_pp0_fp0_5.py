fn = lambda: None
# Test fn.__code__
try:
    fn.__code__
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test fn.__code__ = 1
try:
    fn.__code__ = 1
except TypeError:
    pass
else:
    print('TypeError expected')

# Test fn.__code__ = 1.1
try:
    fn.__code__ = 1.1
except TypeError:
    pass
else:
    print('TypeError expected')

# Test fn.__code__ = 'a'
try:
    fn.__code__ = 'a'
except TypeError:
    pass
else:
    print('TypeError expected')

# Test fn.__code__ = b'a'
try:
    fn.__code__ = b'a'
except TypeError:
    pass
else:
    print('TypeError expected')

# Test fn.__code__ = bytearray(b'a')
try:
    fn.__code__ = bytearray(b'a')
except TypeError
