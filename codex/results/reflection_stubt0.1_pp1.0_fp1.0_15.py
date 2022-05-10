fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24071: __code__ attribute of a function should not be writable
def f(): pass
try:
    f.__code__ = None
except TypeError:
    pass
else:
    print("TypeError not raised")

# Issue #24071: __code__ attribute of a function should not be writable
def f(): pass
try:
    del f.__code__
except TypeError:
    pass
else:
    print("TypeError not raised")

# Issue #24071: __code__ attribute of a function should not be writable
def f(): pass
try:
    f.__code__ = None
except TypeError:
    pass
else:
    print("TypeError not raised")

# Issue #24071: __code__ attribute of a function should not be writable
def f(): pass
try:
    del f.__code__
except TypeError:
    pass
else:
    print("TypeError not raised")

# Issue #24071: __code__ attribute of a function should not be writ
