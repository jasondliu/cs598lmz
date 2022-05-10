fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# test for proper handling of "code" objects
# (see https://github.com/python/cpython/pull/9158)
try:
    fn()
except TypeError:
    pass
else:
    print('FAILED: fn() should have raised a TypeError')

# test for proper handling of "code" objects
# (see https://bugs.python.org/issue33897)
try:
    fn.__code__.co_filename
except TypeError:
    pass
else:
    print('FAILED: fn.__code__.co_filename should have raised a TypeError')

# test for proper handling of "code" objects
try:
    fn.__code__.co_filename = 'foo'
except TypeError:
    pass
else:
    print('FAILED: fn.__code__.co_filename = \'foo\' should have raised a TypeError')

# test for proper handling of "code" objects
try:
    fn.__code__ = None
except TypeError:
    pass
else:
    print('
