fn = lambda: None
# Test fn.__code__
if hasattr(fn, "__code__"):
    print(f"{fn.__code__=}")
    
# Test fn.__dir__
if hasattr(fn, "__dir__"):
    print(f"{fn.__dir__=}")

# Test fn.__dict__
if hasattr(fn, "__dict__"):
    print(f"{fn.__dict__=}")
    
# Test fn.__class__
if hasattr(fn, "__class__"):
    print(f"{fn.__class__=}")

# Test fn.__func__
if hasattr(fn, "__func__"):
    print(f"{fn.__func__=}")
    
# Test fn.__closure__
if hasattr(fn, "__closure__"):
    print(f"{fn.__closure__=}")

# Test fn.__call__
if hasattr(fn, "__call__"):
    print(f"{fn.__call__=}")
    
