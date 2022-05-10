fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #27096: The __code__ attribute of a built-in function should not be
# writable.
def f(): pass
f.__code__ = 42

# Issue #27096: The __code__ attribute of a built-in function should not be
# writable.
def f(): pass
f.__code__ = 42

# Issue #27096: The __code__ attribute of a built-in function should not be
# writable.
def f(): pass
f.__code__ = 42

# Issue #27096: The __code__ attribute of a built-in function should not be
# writable.
def f(): pass
f.__code__ = 42

# Issue #27096: The __code__ attribute of a built-in function should not be
# writable.
def f(): pass
f.__code__ = 42

# Issue #27096: The __code__ attribute of a built-in function should not be
# writable.
def f(): pass
f.__code__ = 42

# Issue
