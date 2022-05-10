fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = None
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = 1
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = 'abc'
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = b'abc'
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = {'abc': 123}
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = [1, 2, 3]
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = (1, 2, 3)
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = {1, 2, 3}

