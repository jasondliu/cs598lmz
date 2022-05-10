fn = lambda: None
# Test fn.__code__
setattr(fn, '__code__', 0)

fn = lambda: None
# Test fn.__closure__
setattr(fn, '__closure__', 0)

# Test closures
def f():
    def g():
        return 1
    a = 1
    return g

t = f()
print(t())

# Test global vars
a = b = c = 0
def f():
    global a, b, c
    a = 1
    b = 2

f()
print(a, b, c)

# Test global vars
# To test global vars declaration before and after
# the function.
a = 0
def f():
    global a
    a = 1

a = 0
f()
print(a)

# Test varargs
def f(a, b, *args):
    print(a, b, args)

f(1, 2)
f(1, 2, 3)
f(1, 2, 3, 4)

# Test keyword args
def f(a, b=3, c=
