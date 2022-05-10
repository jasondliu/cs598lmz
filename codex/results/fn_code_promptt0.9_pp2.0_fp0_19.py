fn = lambda: None
# Test fn.__code__.co_filename == '<string>'
assert fn.__code__.co_filename == '<string>'


def fn():
    pass


# Test fn.__code__.co_filename.endswith('.py')
assert fn.__code__.co_filename.endswith('.py')

# Test fn.__code__.co_filename.split('/')[-1] == 'test.py'
assert fn.__code__.co_filename.split('/')[-1] == 'test.py'

# Test fn.__code__.co_filename == __file__
assert fn.__code__.co_filename == __file__
