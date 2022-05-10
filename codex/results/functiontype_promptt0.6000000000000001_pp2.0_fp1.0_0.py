import types
# Test types.FunctionType
def func1(a, b):
    print(a, b)

print(type(func1))
print(isinstance(func1, types.FunctionType))

# Test types.GeneratorType
def func2():
    yield 1

print(type(func2()))
print(isinstance(func2(), types.GeneratorType))

# Test types.GeneratorType
def func3():
    for i in range(10):
        yield i

print(type(func3()))
print(isinstance(func3(), types.GeneratorType))

# Test types.ClassType

# Test types.TypeType

# Test types.InstanceType

# Test types.NoneType

# Test types.ModuleType

# Test types.FileType

# Test types.BuiltinFunctionType

# Test types.BuiltinMethodType

# Test types.XRangeType

# Test types.SliceType

# Test types.EllipsisType

# Test types.UnboundMethodType

# Test types.ObjectType

# Test types.
