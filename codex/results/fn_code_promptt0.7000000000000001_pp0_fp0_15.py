fn = lambda: None
# Test fn.__code__
code = CodeType(1, 1, 1, 1, "", "", "", (), (), (), "", "", 0, b"")
fn.__code__ = code
# Test fn.__closure__
cell1 = CellType(None)
fn.__closure__ = (cell1,)
# Test fn.__defaults__
defaults = (1, 2)
fn.__defaults__ = defaults
# Test fn.__kwdefaults__
fn.__kwdefaults__ = defaults
# Test fn.__annotations__
annotations = {"a": 1}
fn.__annotations__ = annotations
# Test fn.__globals__
fn.__globals__ = globals()
# Test fn.__dict__
fn.__dict__ = fn.__dict__  # Make sure we don't blow up here.
# Test fn.__name__
fn.__name__ = "test"
# Test fn.__qualname__
fn.__qualname__ = "test"
# Test fn.__module__
fn.__module__ = "test"
# Test fn
