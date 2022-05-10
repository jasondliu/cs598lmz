fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #29091: __code__ attribute of a function should be read-only
def f(): pass
try:
    f.__code__ = None
except TypeError:
    pass
else:
    raise Exception("__code__ attribute should be read-only")

# Issue #29092: __code__ attribute of a function should be a code object
def f(): pass
try:
    f.__code__ = "not a code object"
except TypeError:
    pass
else:
    raise Exception("__code__ attribute should be a code object")

# Issue #29093: __code__ attribute of a function should be a code object
def f(): pass
try:
    f.__code__ = 1
except TypeError:
    pass
else:
    raise Exception("__code__ attribute should be a code object")

# Issue #29094: __code__ attribute of a function should be a code object
def f(): pass
try:
    f.__code__ = 1.0
except TypeError:
    pass
else:
   
