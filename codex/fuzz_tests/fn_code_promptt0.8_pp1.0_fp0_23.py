fn = lambda: None
# Test fn.__code__ property.
fn.__code__    # type: ignore
# Test '__code__' in dir(fn).
'__code__' in dir(fn)

def fn(): pass
# Test fn.__defaults__ property.
fn.__defaults__    # type: ignore
# Test '__defaults__' in dir(fn).
'__defaults__' in dir(fn)

def fn(): pass
# Test fn.__closure__ property.
fn.__closure__    # type: ignore
# Test '__closure__' in dir(fn).
'__closure__' in dir(fn)

def fn(): pass
# Test fn.__globals__ property.
fn.__globals__    # type: ignore
# Test '__globals__' in dir(fn).
'__globals__' in dir(fn)

fn = lambda: None
# Test fn.__kwdefaults__ property.
fn.__kwdefaults__    # type: ignore
# Test '__kwdefaults__' in dir(fn).
'__kwdefaults
