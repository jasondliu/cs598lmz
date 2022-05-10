fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __code__ is a read-only attribute
try:
    fn.__code__ = None
except TypeError:
    pass
else:
    raise Exception("__code__ is not read-only")

# __code__ must be a code object
try:
    fn.__code__ = 1
except TypeError:
    pass
else:
    raise Exception("__code__ must be a code object")

# __code__ must be a code object
try:
    fn.__code__ = "foo"
except TypeError:
    pass
else:
    raise Exception("__code__ must be a code object")

# __code__ must be a code object
try:
    fn.__code__ = 1.0
except TypeError:
    pass
else:
    raise Exception("__code__ must be a code object")

# __code__ must be a code object
try:
    fn.__code__ = []
except TypeError:
    pass
else:
    raise Exception("__code__ must be a code object")

# __code
