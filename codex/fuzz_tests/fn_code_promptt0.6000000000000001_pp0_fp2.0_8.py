fn = lambda: None
# Test fn.__code__.__class__
setattr(fn.__code__, 'co_filename', 'fake')

# Test fn.__code__.co_filename = 'fake'
fn = lambda: None
fn.__code__.co_filename = 'fake'

# Test fn.__code__.co_filename == 'fake'
fn = lambda: None
fn.__code__.co_filename == 'fake'

# Test fn.__code__.co_filename != 'fake'
fn = lambda: None
fn.__code__.co_filename != 'fake'

# Test fn.__code__.co_filename in [ 'fake' ]
fn = lambda: None
fn.__code__.co_filename in [ 'fake' ]

# Test fn.__code__.co_filename not in [ 'fake' ]
fn = lambda: None
fn.__code__.co_filename not in [ 'fake' ]

# Test fn.__code__.co_filename is not None
fn = lambda: None
fn.__code__.co_filename is not None

#
