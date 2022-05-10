fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the code object is not a generator
def fn():
    pass
fn.__code__ = (i for i in ())
fn()

# Test that the code object is not a generator
def fn():
    pass
fn.__code__ = (i for i in ())
fn()

# Test that the code object is not a generator
def fn():
    pass
fn.__code__ = (i for i in ())
fn()

# Test that the code object is not a generator
def fn():
    pass
fn.__code__ = (i for i in ())
fn()

# Test that the code object is not a generator
def fn():
    pass
fn.__code__ = (i for i in ())
fn()

# Test that the code object is not a generator
def fn():
    pass
fn.__code__ = (i for i in ())
fn()

# Test that the code object is not a generator
def fn():
    pass
fn.__code__ = (i for i in ())
fn()

# Test that
