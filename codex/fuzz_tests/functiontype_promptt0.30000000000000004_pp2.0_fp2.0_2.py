import types
# Test types.FunctionType
def f():
    pass

print(type(f) == types.FunctionType)
print(type(lambda: None) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.CodeType
def fn(x, y):
    return x + y

print(type(fn.__code__) == types.CodeType)

# Test types.FrameType
def bar():
    import inspect
    return inspect.currentframe()

print(type(bar()) == types.FrameType)

# Test types.TracebackType
def foo():
    try:
        1/0
    except Exception as e:
        import sys
        return sys.exc_info()[2]

print(type(foo()) == types.TracebackType)

# Test types.ModuleType
import types
print(type(types) == types.ModuleType)

# Test types.BuiltinFunctionType
print(type(len) == types.BuiltinFunctionType)
print(type(iter) ==
