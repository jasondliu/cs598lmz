fn = lambda: None
# Test fn.__code__.co_firstlineno

def f():
    pass

print(f.__code__.co_firstlineno)
# Test fn.__code__.co_consts

def f():
    a = 1
    b = 'x'
    c = (1, 2)

print(f.__code__.co_consts)
# Test fn.__code__.co_names

def f(a, b, c):
    pass

print(f.__code__.co_names)
# Test fn.__code__.co_varnames

def f(a, b, c):
    pass

print(f.__code__.co_varnames)
# Test fn.__code__.co_nlocals

def f(a, b, c):
    x = 1

print(f.__code__.co_nlocals)
# Test fn.__code__.co_varnames

def f():
    # Check that while loop doesn't crash
    while 1:
        pass

f()
