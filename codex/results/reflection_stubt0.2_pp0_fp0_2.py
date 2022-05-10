fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_filename

# Issue #17071: test that __code__ is writable
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #17071: test that __code__ is writable
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #17071: test that __code__ is writable
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #17071: test that __code__ is writable
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #17071: test that __code__ is writable
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #17071: test that __code__ is writable
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #
