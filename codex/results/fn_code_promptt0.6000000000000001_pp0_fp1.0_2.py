fn = lambda: None
# Test fn.__code__.co_filename.
# Should raise AttributeError if no such attribute exists.

try:
    fn.__code__.co_filename
except AttributeError:
    pass
else:
    print('AttributeError expected')
