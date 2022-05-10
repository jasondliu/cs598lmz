fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24095: __code__ should be read-only
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #24096: __code__ should be read-only
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #24097: __code__ should be read-only
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #24098: __code__ should be read-only
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #24099: __code__ should be read-only
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #24100: __code__ should be read-only
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #24101: __code__ should be read-only
def
