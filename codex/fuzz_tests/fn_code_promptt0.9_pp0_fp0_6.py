fn = lambda: None
# Test fn.__code__ attribute use
fn.__code__

# Test type of function's __code__ attribute
assert isinstance(fn.__code__, types.CodeType)

# Test type of function's __globals__ attribute
assert isinstance(fn.__globals__, dict)

# Test type of function's __kwdefaults__ attribute
assert isinstance(fn.__kwdefaults__, dict)

# Test type of function's __defaults__ attribute
assert isinstance(fn.__defaults__, tuple)

# Test function's signature
signature(fn)
