fn = lambda: None
# Test fn.__code__.co_argcount

def f(): pass
print(f.__code__.co_argcount)
def f(a): pass
print(f.__code__.co_argcount)
def f(a, b): pass
print(f.__code__.co_argcount)
def f(a, b, c): pass
print(f.__code__.co_argcount)
def f(a, b, c, d): pass
print(f.__code__.co_argcount)
def f(a, b, c, d, e): pass
print(f.__code__.co_argcount)
def f(a, b, c, d, e, f): pass
print(f.__code__.co_argcount)
def f(a, b, c, d, e, f, g): pass
print(f.__code__.co_argcount)
def f(a, b, c, d, e, f, g, h): pass
print(f.__code__.co_argcount)
def f(a,
