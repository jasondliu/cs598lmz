fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #2360: the __code__ attribute must be a code object
def fn(): pass
fn.__code__ = 'foo'
try:
    fn()
except TypeError:
    pass
else:
    print("TypeError not raised")

# Issue #2360: f_code must be a code object
def fn(): pass
fn.__code__.co_code = 'foo'
try:
    fn()
except TypeError:
    pass
else:
    print("TypeError not raised")

# Issue #2360: f_code must be a code object
def fn(): pass
fn.__code__.co_code = None
try:
    fn()
except TypeError:
    pass
else:
    print("TypeError not raised")

# Issue #2360: f_code must be a code object
def fn(): pass
fn.__code__ = None
try:
    fn()
except TypeError:
    pass
else:
    print("TypeError not raised")

# Issue #2360: f_code must
