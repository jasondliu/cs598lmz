fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that a generator expression can be used as the __code__ attribute of a
# function.
fn = lambda: None
ge = (i for i in ())
fn.__code__ = ge
fn()

# Test that a generator function can be used as the __code__ attribute of a
# function.
fn = lambda: None
gf = (lambda: (yield))()
fn.__code__ = gf
fn()

# Test that a generator function can be used as the __code__ attribute of a
# function.
fn = lambda: None
gf = (lambda: (yield from ()))()
fn.__code__ = gf
fn()

# Test that a generator function can be used as the __code__ attribute of a
# function.
fn = lambda: None
gf = (lambda: (yield from (i for i in ())))()
fn.__code__ = gf
fn()

# Test that a generator function can be used as the __code__ attribute of a
# function.
fn = lambda: None
gf =
