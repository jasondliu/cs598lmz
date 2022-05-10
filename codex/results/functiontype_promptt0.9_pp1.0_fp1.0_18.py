import types
# Test types.FunctionType
print("FunctionType", type(# Remove # before ')')
class C:
    # Remove # before 'def'
        # Remove # before 'return'
        # Remove # before ')'
# Call the method defined in C
d = C()
print(d.f())

print("Callable", callable(d))
# Callable
# True
# Method Type
print("MethodType", type(d.f))
# Output: <type 'instancemethod'>
# Method Type
print("MethodType", isinstance(d.f, types.MethodType))
# Output: True
# Function Type Output
print("FunctionType", isinstance(d.f, types.FunctionType))
# Output: True
# Built-in Function Type
print("BuiltinFunctionType", isinstance(zip, types.BuiltinFunctionType))
# Output: True
# Lambda Type
print("LambdaType", isinstance((lambda x: x**2), types.LambdaType))
# Output: True
# Generator Type
print("GeneratorType", isinstance((x for x in range(10)), types
