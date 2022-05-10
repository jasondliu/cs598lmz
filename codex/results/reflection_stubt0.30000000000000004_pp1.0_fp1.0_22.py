fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the code object of a function is writable
def fn(): pass
fn.__code__ = None
fn()

# Test that the code object of a function is writable
def fn(): pass
fn.__code__ = 42
fn()

# Test that the code object of a function is writable
def fn(): pass
fn.__code__ = "foo"
fn()

# Test that the code object of a function is writable
def fn(): pass
fn.__code__ = fn
fn()

# Test that the code object of a function is writable
def fn(): pass
fn.__code__ = (i for i in ())
fn()

# Test that the code object of a function is writable
def fn(): pass
fn.__code__ = [1, 2, 3]
fn()

# Test that the code object of a function is writable
def fn(): pass
fn.__code__ = {'foo': 'bar'}
fn()

# Test that the code object of a function is writable
def fn(): pass

