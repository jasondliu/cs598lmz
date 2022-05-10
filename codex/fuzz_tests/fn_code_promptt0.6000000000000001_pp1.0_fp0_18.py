fn = lambda: None
# Test fn.__code__.co_varnames

def f():
    a = 1
    b = 2
    c = 3
    d = 4

print(f.__code__.co_varnames)
print(f.__code__.co_argcount)

f()
print(f.__code__.co_varnames)
print(f.__code__.co_argcount)

# Test fn.__code__.co_argcount, co_varnames, co_argcount
def f(a, b, c, d):
    pass

print(f.__code__.co_varnames)
print(f.__code__.co_argcount)

f()
print(f.__code__.co_varnames)
print(f.__code__.co_argcount)

# Test fn.__code__.co_argcount, co_varnames, co_argcount
def f(a, b, c, d):
    a = 1
    b = 2
    c = 3
    d = 4

