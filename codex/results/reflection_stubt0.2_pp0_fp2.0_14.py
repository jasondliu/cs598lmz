fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #22897: __code__ should not be writable on built-in functions
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #22897: __code__ should not be writable on built-in methods
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #22897: __code__ should not be writable on built-in methods
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #22897: __code__ should not be writable on built-in methods
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #22897: __code__ should not be writable on built-in methods
def f(): pass
def g(): pass
f.__code__ = g.__code__

# Issue #22897: __code__ should not be writable on built-in methods
def f(): pass
def g
