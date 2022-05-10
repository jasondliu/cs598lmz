fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __code__ = None
fn = lambda: None
fn.__code__ = None
fn()

# __code__ = str
fn = lambda: None
fn.__code__ = 'a'
fn()

# __code__ = 1
fn = lambda: None
fn.__code__ = 1
fn()

# __code__ = float('nan')
fn = lambda: None
fn.__code__ = float('nan')
fn()

# __code__ = float('inf')
fn = lambda: None
fn.__code__ = float('inf')
fn()

# __code__ = -float('inf')
fn = lambda: None
fn.__code__ = -float('inf')
fn()

# __code__ = float('nan')
fn = lambda: None
fn.__code__ = float('nan')
fn()

# __code__ = {'a': 'b'}
fn = lambda: None
fn.__code__ = {'a': 'b'}
fn()

# __code__ = {
