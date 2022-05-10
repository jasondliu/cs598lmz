fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# The line below passes if the optimization is not present.
fn()

# The line below passes if the optimization is present.
fn.__code__.gi_running = True
fn()

# The line below passes if the optimization is not present.
fn.__code__.gi_running = False
fn()

# The line below passes if the optimization is present.
fn.__code__.__code__.co_consts = (1,)
fn()

# The line below passes if the optimization is not present.
fn.__code__.__code__.co_consts = (1, 2)
fn()

# The line below passes if the optimization is present.
fn.__code__.__code__.co_code = b''
fn()

# The line below passes if the optimization is not present.
fn.__code__.__code__.co_code = b'\x00\x00\x00\x00\x00\x00'
fn()
