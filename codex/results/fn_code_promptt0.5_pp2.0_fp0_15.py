fn = lambda: None
# Test fn.__code__.co_varnames
def f():
    a = 1
    b = 2
    c = 3
    return a, b, c

print(f.__code__.co_varnames)
print(f.__code__.co_argcount)
# Test fn.__code__.co_argcount
def f(a, b=1, c=2):
    return a, b, c

print(f.__code__.co_argcount)
# Test fn.__code__.co_consts
def f():
    return 1, "Hello", None

print(f.__code__.co_consts)
# Test fn.__code__.co_nlocals
def f():
    a = 1
    b = 2
    c = 3
    return a, b, c

print(f.__code__.co_nlocals)
# Test fn.__code__.co_stacksize
def f():
    a = 1
    b = 2
    c = 3
    return a, b, c

print
