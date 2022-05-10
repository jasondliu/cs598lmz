fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the code object is not modified if it is not a generator
fn = lambda: None
fn.__code__ = fn.__code__
fn()

# Test that the code object is not modified if it is not a generator
fn = lambda: None
fn.__code__ = fn.__code__
fn()

# Test that the code object is not modified if it is not a generator
fn = lambda: None
fn.__code__ = fn.__code__
fn()

# Test that the code object is not modified if it is not a generator
fn = lambda: None
fn.__code__ = fn.__code__
fn()

# Test that the code object is not modified if it is not a generator
fn = lambda: None
fn.__code__ = fn.__code__
fn()

# Test that the code object is not modified if it is not a generator
fn = lambda: None
fn.__code__ = fn.__code__
fn()

# Test that the code object is not modified if it is not a generator
fn = lambda:
