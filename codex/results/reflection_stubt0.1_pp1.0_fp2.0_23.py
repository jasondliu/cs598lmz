fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23984: __code__ attribute of a function should be read-only
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #23984: __code__ attribute of a function should be read-only
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #23984: __code__ attribute of a function should be read-only
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #23984: __code__ attribute of a function should be read-only
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #23984: __code__ attribute of a function should be read-only
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #23984: __code__ attribute of a function should be read-only
def f(): pass
def g(): pass
f.__
