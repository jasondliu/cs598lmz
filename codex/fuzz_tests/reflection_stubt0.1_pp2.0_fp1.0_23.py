fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24073: __code__ should be read-only
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #24073: __code__ should be read-only
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #24073: __code__ should be read-only
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #24073: __code__ should be read-only
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #24073: __code__ should be read-only
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #24073: __code__ should be read-only
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #24073: __code__ should be read-
