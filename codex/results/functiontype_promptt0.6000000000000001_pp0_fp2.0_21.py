import types
# Test types.FunctionType
print(dir(types.FunctionType))
print(types.FunctionType)
print(type(type(types.FunctionType)))
print(bool(types.FunctionType))
print(bool(type(types.FunctionType)))
print(type(True))
print(type(True) == type(bool(types.FunctionType)))
print(type(types.FunctionType) == type(bool(types.FunctionType)))
print(type(bool(types.FunctionType)) == type(bool(type(types.FunctionType))))
print(type(type(types.FunctionType)) == type(bool(type(types.FunctionType))))
print(type(type(types.FunctionType)) == type(bool(types.FunctionType)))

# Test types.ModuleType
print(dir(types.ModuleType))
print(types.ModuleType)
print(type(type(types.ModuleType)))
print(bool(types.ModuleType))
print(bool(type(types.ModuleType)))
print(type(True))
print(type(True) == type(bool(types.ModuleType)))
print(type(
