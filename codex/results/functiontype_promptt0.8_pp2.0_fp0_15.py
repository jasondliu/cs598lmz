import types
# Test types.FunctionType working
def func():
    return

print isinstance(func, types.FunctionType)

# Type of Module
import sys
print isinstance(sys, types.ModuleType)

# Test types.LambdaType working
func = lambda: "foo"
print isinstance(func, types.LambdaType)

# Type of None
print isinstance(None, types.NoneType)

# Test types.GeneratorType working
g = ("foo" for x in range(5))
print isinstance(g, types.GeneratorType)
