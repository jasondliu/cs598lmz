import types
# Test types.FunctionType, types.LambdaType, types.GeneratorType, types.CodeType
def f():
    pass

def g():
    yield 1

def h():
    return lambda: None

print(type(f) is types.FunctionType)
print(type(g) is types.FunctionType)
print(type(h) is types.FunctionType)
print(type(f.__code__) is types.CodeType)
print(type(g.__code__) is types.CodeType)
print(type(h.__code__) is types.CodeType)
print(type(f()) is types.GeneratorType)
print(type(g()) is types.GeneratorType)
print(type(h()) is types.LambdaType)
