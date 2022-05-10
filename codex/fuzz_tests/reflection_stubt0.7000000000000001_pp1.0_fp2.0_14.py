fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Pointer to code object
fn = lambda: None
fn.__code__ = id(fn.__code__)
fn()

# Very large code object
fn = lambda: None
fn.__code__ = [None] * 0x100000
fn()

# Code object with bad magic number
fn = lambda: None
fn.__code__.co_magic = 0
fn()

# Code object with bad flags
fn = lambda: None
fn.__code__.co_flags = 0
fn()

# Code object with too few constants
fn = lambda: None
fn.__code__.co_consts = [None]
fn()

# Code object with too few names
fn = lambda: None
fn.__code__.co_names = [None]
fn()

# Code object with too few varnames
fn = lambda: None
fn.__code__.co_varnames = [None]
fn()

# Code object with too few freevars
fn = lambda: None
fn.__code__.co_freev
