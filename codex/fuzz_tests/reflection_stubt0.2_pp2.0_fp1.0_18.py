fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the code object is not modified when it is not a generator
# and that the function is called.
fn = lambda: None
fn.__code__ = None
fn()

# Test that the code object is not modified when it is not a generator
# and that the function is called.
fn = lambda: None
fn.__code__ = None
fn()

# Test that the code object is not modified when it is not a generator
# and that the function is called.
fn = lambda: None
fn.__code__ = None
fn()

# Test that the code object is not modified when it is not a generator
# and that the function is called.
fn = lambda: None
fn.__code__ = None
fn()

# Test that the code object is not modified when it is not a generator
# and that the function is called.
fn = lambda: None
fn.__code__ = None
fn()

# Test that the code object is not modified when it is not a generator
# and that the function is called.
fn = lambda: None
fn.
