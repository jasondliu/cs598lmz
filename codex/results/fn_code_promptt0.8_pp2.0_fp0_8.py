fn = lambda: None
# Test fn.__code__ and fn.__closure__.
fn.__code__ = None
fn.__closure__ = None

class Cls:
    # Test Cls.__call__.
    __call__ = lambda: None
    # Test Cls.__new__.
    __new__ = lambda cls: None
    # Test Cls.__init__
    def __init__(self):
        pass

# Test Cls.__class__.
Cls.__class__
# Test Cls.__class__.__class__.
Cls.__class__.__class__

# Test Cls().__class__.
Cls().__class__
# Test Cls().__class__.__class__.
Cls().__class__.__class__

# Now test a call.
fn()

# Test fn.__call__.
fn.__call__()
# Test fn.__class__.
fn.__class__()
# Test fn.__class__.__call__.
fn.__class__.__call__()
# Test fn.__class__
