fn = lambda: None
# Test fn.__code__
fn.__code__ = "__codeslice__"
# Test fn.__closure__
fn.__closure__ = "__closure__"
# Test fn.__name__
fn.__name__ = "__namelower__"
# Test fn.__globals__
fn.__globals__ = "__globals__"
# Test fn.__dict__
fn.__dict__ = "__diclower__"
# Test fn.__annotations__
fn.__annotations__ = "__annotationslower__"
# Test fn.__defaults__
fn.__defaults__ = "__defaultsslower__"
# Test fn.__kwdefaults__
fn.__kwdefaults__ = "__kwdefaultslower__"
# Test fn.__qualname__
fn.__qualname__ = "__qualname__"
# Test fn.__repr__
fn.__repr__ = "__repr__"
# Test fn.__text_signature__
fn.__text_signature__ = "__text_signature__"

