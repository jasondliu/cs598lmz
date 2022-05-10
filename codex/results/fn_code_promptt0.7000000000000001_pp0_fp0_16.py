fn = lambda: None
# Test fn.__code__.co_varnames
def fn():
    return 1
print(fn.__code__.co_varnames)

def fn():
    a = 1
    b = 2
    return a + b
print(fn.__code__.co_varnames)

def fn(a, b, c=3, d=4):
    return a + b + c + d
print(fn.__code__.co_varnames)

def fn(*args):
    return args
print(fn.__code__.co_varnames)

def fn(**kwargs):
    return kwargs
print(fn.__code__.co_varnames)
fn = lambda: None
# Test fn.__code__.co_argcount
def fn():
    return 1
print(fn.__code__.co_argcount)

def fn():
    a = 1
    b = 2
    return a + b
print(fn.__code__.co_argcount)

def fn(a, b, c=3, d=4
