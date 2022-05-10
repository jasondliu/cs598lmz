import types
# Test types.FunctionType and types.BuiltinFunctionType

def function():
        pass

f = function

print type(function)
print type(f)
print type(lambda: None)
print type(dir)
print type(dir(dir))
print type(type)
