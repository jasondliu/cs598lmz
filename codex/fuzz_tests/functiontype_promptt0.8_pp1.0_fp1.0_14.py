import types
# Test types.FunctionType(code, globals, name, argdefs, closure)

def f(a, b=1, *args, **kwargs):
    pass

def g(a, b=1, *args, **kwargs):
    pass

def h(a, b=1, *args, **kwargs):
    pass

def test():
    f(g(h(a=1, b=2), b=3), 4, 5)

code = test.__code__
print(code)

# Make a copy of the code object
code2 = types.FunctionType(code, globals(), "test2", (1, 2), None)
print(code2)

# Try calling code object directly
test2 = code2
print(test2(6, b=7, *(8, 9), **{'A': 10, 'B': 11}))
