fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Call a function with a generator as the code object
# Exception: TypeError: 'generator' object is not callable
fn()

# The same, but with a function
gi = (i for i in ())
fn.__code__ = fn.__code__.__code__
fn()

# The same, but with a function
gi = (i for i in ())
fn.__code__ = fn.__code__.__code__
fn()

# The same, but with a function
gi = (i for i in ())
fn.__code__ = fn.__code__.__code__
fn()

# The same, but with a function
gi = (i for i in ())
fn.__code__ = fn.__code__.__code__
fn()

# The same, but with a function
gi = (i for i in ())
fn.__code__ = fn.__code__.__code__
fn()

# The same, but with a function
gi = (i for i in ())
fn.__code__ = fn.__code__
