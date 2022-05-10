import types
# Test types.FunctionType
# Non-trivial function, nested function
def f(): pass
x = types.FunctionType(f.__code__, f.__globals__, 'g', f.__defaults__)

x()
# Non-trivial function, nested function, with local state
y = types.FunctionType(x.__code__, x.__globals__, x.__name__, x.__defaults__, x.__closure__)

y()
