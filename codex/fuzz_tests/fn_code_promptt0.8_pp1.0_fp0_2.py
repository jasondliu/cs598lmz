fn = lambda: None
# Test fn.__code__
fn.__code__
fn.__code__ = lambda: None
# Test fn.__code__.co_filename
fn.__code__.co_filename
# Test fn.__code__.co_firstlineno
fn.__code__.co_firstlineno
# Test fn.__code__.co_flags
fn.__code__.co_flags
# Test fn.__code__.co_lnotab
fn.__code__.co_lnotab

# Test fn.__code__.co_filename
@decorator
def fn(): pass
fn.__code__.co_filename

# Test fn.__code__.co_firstlineno
@decorator
def fn(): pass
fn.__code__.co_firstlineno

# Test fn.__code__.co_flags
@decorator
def fn(): pass
fn.__code__.co_flags

# Test fn.__code__.co_lnotab
@decorator
def fn(): pass
fn.__code__.co_lnotab

#
