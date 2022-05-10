fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test __closure__ can be None
def fn():
    yield
fn.__code__.__closure__ = None
fn()

# Test __code__ can be None
def fn(): pass
fn.__code__ = None
fn()

# Test __defaults__ can be None
def fn(i=None): pass
fn.__code__.__defaults__ = None
fn()

# Test __dict__ can be None
def fn(): pass
fn.__dict__ = None
fn()

# Test __globals__ can be None
def fn(): pass
fn.__code__.__globals__ = None
fn()

# Test __name__ can be None
def fn(): pass
fn.__name__ = None
fn()

# Test __doc__ can be None
def fn(): pass
fn.__doc__ = None
fn()

# Test __module__ can be None
def fn(): pass
fn.__module__ = None
fn()

# Test __qualname__ can be None
def fn(): pass
fn
