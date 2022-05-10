fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# should now raise a RuntimeError
print('should now raise a RuntimeError')
fn = lambda: None
fn.__code__ = None
fn()

# should now raise a TypeError
print('should now raise a TypeError')
fn = lambda: None
fn.__code__ = object()
fn()

# should now raise a RuntimeError
print('should now raise a RuntimeError')
fn = lambda: None
fn.__code__ = (i for i in ())
fn()

# should now raise a RuntimeError
print('should now raise a RuntimeError')
fn = lambda: None
fn.__code__ = type(lambda: None)
fn()

# should now raise a RuntimeError
print('should now raise a RuntimeError')
fn = lambda: None
fn.__code__ = type(type(lambda: None))
fn()

# should now raise a RuntimeError
print('should now raise a RuntimeError')
fn = lambda: None
fn.__code__ = type(type(type(lambda: None)))
fn()

# should now raise a
