fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23647: Don't crash when a code object is created with a generator
# instead of a tuple for the co_consts attribute.
def fn():
    yield
fn.__code__ = (i for i in ())
fn()

# Issue #23647: Don't crash when a code object is created with a generator
# instead of a tuple for the co_consts attribute.
def fn():
    yield
fn.__code__ = (i for i in ())
fn()

# Issue #23647: Don't crash when a code object is created with a generator
# instead of a tuple for the co_consts attribute.
def fn():
    yield
fn.__code__ = (i for i in ())
fn()

# Issue #23647: Don't crash when a code object is created with a generator
# instead of a tuple for the co_consts attribute.
def fn():
    yield
fn.__code__ = (i for i in ())
fn()

# Issue #23647: Don't crash when a code object is created with a generator
#
