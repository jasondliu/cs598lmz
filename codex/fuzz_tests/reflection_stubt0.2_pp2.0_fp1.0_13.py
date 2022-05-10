fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23984: __code__ setter should not accept a generator
def fn():
    pass
gi = (i for i in ())
try:
    fn.__code__ = gi
except TypeError:
    pass
else:
    raise Exception("__code__ setter should not accept a generator")

# Issue #23984: __code__ setter should not accept a generator
def fn():
    pass
gi = (i for i in ())
try:
    fn.__code__ = gi
except TypeError:
    pass
else:
    raise Exception("__code__ setter should not accept a generator")

# Issue #23984: __code__ setter should not accept a generator
def fn():
    pass
gi = (i for i in ())
try:
    fn.__code__ = gi
except TypeError:
    pass
else:
    raise Exception("__code__ setter should not accept a generator")

# Issue #23984: __code__ setter should not accept a generator
def fn():
   
