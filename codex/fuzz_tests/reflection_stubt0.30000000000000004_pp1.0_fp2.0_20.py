fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #18056: __code__ must be a code object
def fn(): pass
fn.__code__ = None
try:
    fn()
except TypeError:
    pass
else:
    print("TypeError not raised")

# Issue #18056: __code__ must be a code object
def fn(): pass
fn.__code__ = 42
try:
    fn()
except TypeError:
    pass
else:
    print("TypeError not raised")

# Issue #18056: __code__ must be a code object
def fn(): pass
fn.__code__ = "foo"
try:
    fn()
except TypeError:
    pass
else:
    print("TypeError not raised")

# Issue #18056: __code__ must be a code object
def fn(): pass
fn.__code__ = ()
try:
    fn()
except TypeError:
    pass
else:
    print("TypeError not raised")

# Issue #18056: __code__ must be a code object
def fn
