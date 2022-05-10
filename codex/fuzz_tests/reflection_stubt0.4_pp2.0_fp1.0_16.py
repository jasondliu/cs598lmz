fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #19301: __code__ should be read-only
def fn(): pass
c = fn.__code__
try:
    c.__code__ = c
except TypeError:
    pass
else:
    raise Exception("__code__ should be read-only")

# Issue #19301: __code__ should be read-only
def fn(): pass
c = fn.__code__
try:
    c.co_code = b""
except TypeError:
    pass
else:
    raise Exception("__code__ should be read-only")

# Issue #19301: __code__ should be read-only
def fn(): pass
c = fn.__code__
try:
    c.co_consts = ()
except TypeError:
    pass
else:
    raise Exception("__code__ should be read-only")

# Issue #19301: __code__ should be read-only
def fn(): pass
c = fn.__code__
try:
    c.co_filename = ""
except TypeError:
    pass

