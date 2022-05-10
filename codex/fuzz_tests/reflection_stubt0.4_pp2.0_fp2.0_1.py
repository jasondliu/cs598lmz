fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Check that the code object of a function is read-only
def fn():
    pass
fn.__code__ = None

# Check that the code object of a function is read-only
def fn():
    pass
fn.__code__ = 0

# Check that the code object of a function is read-only
def fn():
    pass
fn.__code__ = 0.0

# Check that the code object of a function is read-only
def fn():
    pass
fn.__code__ = ''

# Check that the code object of a function is read-only
def fn():
    pass
fn.__code__ = ()

# Check that the code object of a function is read-only
def fn():
    pass
fn.__code__ = []

# Check that the code object of a function is read-only
def fn():
    pass
fn.__code__ = {}

# Check that the code object of a function is read-only
def fn():
    pass
fn.__code__ = set()

# Check that the code
