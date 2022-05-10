fn = lambda: None
# Test fn.__code__ is an instance of CodeType
setattr(fn, '__code__', 1)

# Test fn.__closure__ is an instance of tuple
setattr(fn, '__closure__', 1)

# Test fn.__closure__[0] is an instance of CellType
fn.__closure__ = (1,)

# Test fn.__annotations__ is an instance of dict
setattr(fn, '__annotations__', 1)

# Test fn.__kwdefaults__ is an instance of dict
setattr(fn, '__kwdefaults__', 1)

# Test fn.__dict__ is an instance of dict
setattr(fn, '__dict__', 1)

# Test fn.__globals__ is an instance of dict
setattr(fn, '__globals__', 1)

# Test fn.__defaults__ is an instance of tuple
setattr(fn, '__defaults__', 1)

# Test fn.__name__ is an instance of str or None
setattr(fn, '__name__', 1)

# Test fn
