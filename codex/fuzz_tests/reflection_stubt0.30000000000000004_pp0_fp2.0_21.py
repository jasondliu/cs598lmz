fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the interpreter can handle a generator with a code object that
# has a non-tuple freevars.
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the interpreter can handle a generator with a code object that
# has a non-tuple cellvars.
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the interpreter can handle a generator with a code object that
# has a non-tuple cellvars.
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the interpreter can handle a generator with a code object that
# has a non-tuple cellvars.
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the interpreter can handle a generator with a code object that
# has a non-tuple cellvars.
fn
