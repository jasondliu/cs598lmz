import types
# Test types.FunctionType

def fn():
    pass

print(type(fn))
print(type(fn) == types.FunctionType)
print(type(fn) is types.FunctionType)
print(type(fn) is types.FunctionType)
print(type(fn) == types.BuiltinFunctionType)
print(type(fn) is types.BuiltinFunctionType)
print(type(fn) == types.BuiltinMethodType)
print(type(fn) is types.BuiltinMethodType)
print(type(fn) == types.MethodType)
print(type(fn) is types.MethodType)
print(type(fn) == types.LambdaType)
print(type(fn) is types.LambdaType)
print(type(fn) == types.GeneratorType)
print(type(fn) is types.GeneratorType)
print(type(fn) == types.CodeType)
print(type(fn) is types.CodeType)

# Test types.MethodType

class C:
    def fn(self):
        pass

c = C()

