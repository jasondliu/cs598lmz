import types
# Test types.FunctionType
print(type(foo) is types.FunctionType)
# Test types.MethodType
print(type(bar) is types.MethodType)
# Test types.BuiltinFunctionType
print(type(print) is types.BuiltinFunctionType)
# Test types.BuiltinMethodType
print(type(list.insert) is types.BuiltinMethodType)
# Test types.LambdaType
print(type(lambda: None) is types.LambdaType)
# Test types.GeneratorType
print(type(range(0)) is types.GeneratorType)


# Idiomatic Code
# Section 11.10
print('#' * 52 + '  #')
print('#' * 52 + '  Idiomatic Code')
print('#' * 52 + '  #')

# Is Subclass
print(object.__subclasses__())
print('#' * 52 + '  #')
print(isinstance(1, int))
print(issubclass(int, object))
# int is a direct subclass of object
# int is a subclass of object
print('#
