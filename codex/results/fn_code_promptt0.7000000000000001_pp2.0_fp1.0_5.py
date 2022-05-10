fn = lambda: None
# Test fn.__code__ is not None
fn.__code__ = None
# Test fn.__code__.co_filename is not None
fn.__code__.co_filename = None
# Test fn.__code__.co_firstlineno is not None
fn.__code__.co_firstlineno = None
# Test fn.__globals__ is not None
fn.__globals__ = None
# Test fn.__globals__['__name__'] is not None
fn.__globals__['__name__'] = None
# Test fn.__globals__['__file__'] is not None
fn.__globals__['__file__'] = None
# Test fn.__module__ is not None
fn.__module__ = None
# Test fn.__qualname__ is not None
fn.__qualname__ = None

# Test method is not None
fn = lambda: None
fn.method = None

# Test class is not None
class cls:
    pass

cls = None

# Test class.__dict__ is not None
cls
