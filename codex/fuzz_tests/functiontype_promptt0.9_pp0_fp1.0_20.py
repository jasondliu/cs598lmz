import types
# Test types.FunctionType
## Test 1
print(type(abs)==types.BuiltinFunctionType)
## Test 2
print(type(int)==types.BuiltinFunctionType)
## Test 3
print(type(lambda x: x)==types.LambdaType)
## Test 4
print(type((x for x in range(10)))==types.GeneratorType)

print('------Test类型判断------')
from types import *
# Test types.FunctionType
## Test 1
print(type(abs)==BuiltinFunctionType)
## Test 2
print(type(int)==BuiltinFunctionType)
## Test 3
print(type(lambda x: x)==LambdaType)
## Test 4
print(type((x for x in range(10)))==GeneratorType)
