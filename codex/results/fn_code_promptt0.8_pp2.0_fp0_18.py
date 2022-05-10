fn = lambda: None
# Test fn.__code__
fn.__code__ = ""

# Test fn.__globals__
fn.__globals__ = {}

# Test fn.__closure__
fn.__closure__ = ()

# Test fn.__annotations__
fn.__annotations__ = {}
