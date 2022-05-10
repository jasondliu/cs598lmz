fn = lambda: None
# Test fn.__code__.co_freevars and fn.__closure__
def f(a, b):
    def g(c):
        c = a + b
        return c
    return g

# Test fn.__code__.co_cellvars and fn.__closure__
def h(x):
    y = x
    def g():
        return y
    return g

# Test fn.__code__.co_freevars and fn.__closure__
def f2(obj, value):
    def g():
        obj.x = value
    return g

# Test fn.__code__.co_freevars and fn.__closure__, part 2
def f3(x, y):
    def g(z):
        def h(q):
            return x + y + z + q
        return h
    return g

# Test multiple free vars, including one in a nested scope
def f4(f, a, b):
    def g(c):
        def h(d):
            return f(a, b, c, d)
        return h
