import types
# Test types.FunctionType()
# Funcion types
def func_string():
    print('I am a function string')

print(func_string)
print(type(func_string))
print(isinstance(func_string, types.FunctionType))

# Function variables
func_string_2 = func_string
print(func_string_2)
print(type(func_string_2))
print(isinstance(func_string_2, types.FunctionType))

# Anonymous function
func_lambda = lambda x, y, z: x + y + z
print(func_lambda)
print(type(func_lambda))
print(isinstance(func_lambda, types.FunctionType))

# Test types.LambdaType()
print(isinstance(func_lambda, types.LambdaType))
print(isinstance(func_string, types.LambdaType))

# Test types.BuiltinFunctionType()
print(isinstance(print, types.BuiltinFunctionType))
print(isinstance(func_string, types.BuiltinFunctionType))

# Test types.Gener
