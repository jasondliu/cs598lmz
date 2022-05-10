fn = lambda: None
# Test fn.__code__.co_varnames
def f():
    x = 1
    y = 2
    z = 3
print(f.__code__.co_varnames)
print(f.__code__.co_argcount)

# Test fn.__code__.co_argcount
def f(x):
    y = 2
    z = 3
print(f.__code__.co_varnames)
print(f.__code__.co_argcount)

# Test fn.__defaults__
def f(x, y=3, z=4):
    pass
print(f.__defaults__)

# Test fn.__kwdefaults__
def f(x, y=3, *, z=4):
    pass
print(f.__kwdefaults__)

# Test fn.__annotations__
def f(x: 'spam', y: (1, 10)=5, *, z: float):
    pass
print(f.__annotations__)

# Test fn.__closure__
def make_adder(x
