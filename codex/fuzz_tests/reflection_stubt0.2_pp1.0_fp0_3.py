fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __code__ can be a function
fn = lambda: None
fn.__code__ = lambda: None
fn()

# __code__ can be a function with a __code__
fn = lambda: None
fn.__code__ = lambda: None
fn.__code__.__code__ = lambda: None
fn()

# __code__ can be a function with a __code__ with a __code__
fn = lambda: None
fn.__code__ = lambda: None
fn.__code__.__code__ = lambda: None
fn.__code__.__code__.__code__ = lambda: None
fn()

# __code__ can be a function with a __code__ with a __code__ with a __code__
fn = lambda: None
fn.__code__ = lambda: None
fn.__code__.__code__ = lambda: None
fn.__code__.__code__.__code__ = lambda: None
fn.__code__.__code__.__code__.__code__ = lambda: None
fn()

# __
