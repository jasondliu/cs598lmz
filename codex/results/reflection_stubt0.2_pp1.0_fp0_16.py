fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24078: __code__ setter should not accept a generator
def fn(): pass
gi = (i for i in ())
try:
    fn.__code__ = gi
except TypeError:
    pass
else:
    print("Failed to raise TypeError")

# Issue #24078: __code__ setter should not accept a generator
def fn(): pass
gi = (i for i in ())
try:
    fn.__code__ = gi
except TypeError:
    pass
else:
    print("Failed to raise TypeError")

# Issue #24078: __code__ setter should not accept a generator
def fn(): pass
gi = (i for i in ())
try:
    fn.__code__ = gi
except TypeError:
    pass
else:
    print("Failed to raise TypeError")

# Issue #24078: __code__ setter should not accept a generator
def fn(): pass
gi = (i for i in ())
try:
    fn.__code__ = gi
