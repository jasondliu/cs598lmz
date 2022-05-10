import types
# Test types.FunctionType

def f():
    pass

x = types.FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__)
print(x.__name__)
print(x.__defaults__)
print(x.__closure__)
print(x.__code__)
print(x.__globals__)
print(x())

x = types.FunctionType(f.__code__, f.__globals__, "newname", f.__defaults__, f.__closure__)
print(x.__name__)
print(x.__defaults__)
print(x.__closure__)
print(x.__code__)
print(x.__globals__)
print(x())

x = types.FunctionType(f.__code__, f.__globals__, f.__name__, (1,), f.__closure__)
print(x.__name__)
print(x.__defaults__)

