fn = lambda: None
# Test fn.__code__ is None and fn.__defaults__ is a tuple
_ = fn.__code__
_ = fn.__defaults__

# Test that we can access the __closure__
def outer():
    a = 1
    b = 2
    def inner():
        return a + b
    return inner
fn = outer()
_ = fn.__closure__

# Test that we can access the __globals__
def fn():
    return 1
_ = fn.__globals__

# Test that we can get the module
def fn():
    return 1
_ = fn.__module__

# Test that we can call the fn
def fn():
    return 1
_ = fn()

# Test that we can return functions
def fn():
    return fn
