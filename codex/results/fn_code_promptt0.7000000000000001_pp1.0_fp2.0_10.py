fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__ = None
fn.__code__ = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = None
# Test fn.__code__.co_filename
fn.__code__.co_filename = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename = 'abc'

# Test fn.__code__.co_filename
fn.__code__.co_filename = lambda: 'abc'

# Test fn.__code__.co_filename
fn.__code__.co_filename = lambda: None

# Test fn.__code__.co_filename
fn.__code__.co_filename = lambda: validate_file('abc')

# Test fn.__code__.co_filename
fn.__code__.co_filename = lambda: validate_file(None)

# Test fn.__code__.co_filename
fn.__code__.co_filename = lambda: validate_file(lambda: 'abc')


