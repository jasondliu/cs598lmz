fn = lambda: None
# Test fn.__code__.co_flags
fn.__code__ = types.CodeType(
    0, 0, 0, 0, b"c", (), (), (), "", "", 1, b"", (), (), ()
)
# Test fn.__globals__
fn.__globals__ = {}
# Test fn.__closure__
fn.__closure__ = (None,)
# Test fn.__dict__
fn.__dict__ = {}
# Test fn.__kwdefaults__
fn.__kwdefaults__ = {}
# Test fn.__annotations__
fn.__annotations__ = {}
# Test fn.__qualname__
fn.__qualname__ = ""

# Test fn.__module__
fn.__module__ = "foo"
# Test fn.__defaults__
fn.__defaults__ = ()
# Test fn.__code__.co_varnames
fn.__code__ = types.CodeType(
    0, 0, 0, 0, b"c", ("x",), (), (), "", "", 1, b"", (), (), ()
)

