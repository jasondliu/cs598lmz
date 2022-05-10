import types
# Test types.FunctionType

print(types.FunctionType)

def foo():
    pass

bar = types.FunctionType(foo.__code__, foo.__globals__)
print(bar is foo)

# Test types.BuiltinFunctionType
if is_cli:
    print(types.BuiltinFunctionType)

import sys
print(types.BuiltinFunctionType is types.FunctionType)
print(types.BuiltinFunctionType(sys.getrecursionlimit))
