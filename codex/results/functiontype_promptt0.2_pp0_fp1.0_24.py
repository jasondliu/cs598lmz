import types
# Test types.FunctionType
def func():
    pass

print(type(func) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.LambdaType
print(isinstance(abs, types.BuiltinFunctionType))
print(isinstance(func, types.FunctionType))
print(isinstance(lambda x: x, types.LambdaType))

# Test types.GeneratorType
print(isinstance((x for x in range(10)), types.GeneratorType))

# Test types.NoneType
print(type(None) == types.NoneType)

# Test types.SliceType
print(type(slice(1, 10, 2)) == types.SliceType)

# Test types.EllipsisType
print(type(Ellipsis) == types.EllipsisType)

# Test types.NotImplementedType
print(type(NotImple
