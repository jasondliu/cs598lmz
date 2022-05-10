fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# This should raise a TypeError.
fn.__code__ = None
fn()

# This should raise a TypeError.
fn.__code__ = 1
fn()

# This should raise a TypeError.
fn.__code__ = 'a'
fn()

# This should raise a TypeError.
fn.__code__ = {}
fn()

# This should raise a TypeError.
fn.__code__ = []
fn()

# This should raise a TypeError.
fn.__code__ = (lambda: None).__code__
fn()

# This should raise a TypeError.
fn.__code__ = type(lambda: None).__code__
fn()

# This should raise a TypeError.
fn.__code__ = type(gi).__code__
fn()

# This should raise a TypeError.
fn.__code__ = type(gi).__new__(type(gi))
fn()

# This should raise a TypeError.
fn.__code__ = type(gi).__new
