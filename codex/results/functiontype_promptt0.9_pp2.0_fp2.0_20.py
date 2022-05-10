import types
# Test types.FunctionType here.

# Test a simple function declared with def
def f0(): pass
assert type(f0) is types.FunctionType

# Test a simple nested function declared with def
def f1():
    def g(): pass
    assert type(g) is types.FunctionType
f1()

# Test a simple function declared with lambda
g = lambda: None
assert type(g) is types.FunctionType

# Test a simple nested function declared with lambda
def f2():
    g = lambda: None
    assert type(g) is types.FunctionType
f2()

# Issue 559: nested closures have a __closure__ attribute
def f():
    x = "foo"
    def g():
        return x
    return g

g = f()
assert hasattr(g, "__closure__")
print("Success")
