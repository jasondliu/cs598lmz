fn = lambda: None
# Test fn.__code__
try:
    fn.__code__
except AttributeError:
    print('SKIP')
    raise SystemExit

# simple function
def foo():
    pass

# nested function
def bar():
    def foo():
        pass

# nested function with closure
def bar():
    x = 42
    def foo():
        pass
    return foo

# nested function with closure that assigns to outer var
def bar():
    x = 42
    def foo():
        nonlocal x
        x = -1
    return foo

# nested function with closure that assigns to outer var and accesses outer var
def bar():
    x = 42
    def foo():
        nonlocal x
        x = -1
        return x
    return foo

# nested function with closure that assigns to outer var and accesses outer var
def bar():
    x = 42
    def foo():
        nonlocal x
        x = -1
        return x
        return x
    return foo

# nested function with closure that assigns to outer var and accesses outer var
def bar():
    x =
