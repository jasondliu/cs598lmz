import weakref
# Test weakref.ref with a function object.
def f():
    pass
r = weakref.ref(f)
r()

# Test weakref.ref with a lambda expression.
r = weakref.ref(lambda: None)
r()

# Test weakref.ref with a nested function.
def f():
    def g():
        pass
    return g
r = weakref.ref(f)
r()

# Test weakref.ref with a function object with a cycle.
def f():
    pass
f.attr = f
r = weakref.ref(f)
r()

# Test weakref.ref with a lambda expression with a cycle.
def f():
    return (lambda: None)
f.attr = f
r = weakref.ref(f)
r()

# Test weakref.ref with a nested function with a cycle.
def f():
    def g():
        pass
    g.attr = g
    return g
r = weakref.ref(f)
r()
