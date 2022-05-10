import types
# Test types.FunctionType
def func(a):
    return a

print(type(func))
print(types.FunctionType)
print(type(func) == types.FunctionType)

# Test types.LambdaType
lamb = lambda a: a
print(type(lamb))
print(types.LambdaType)
print(type(lamb) == types.LambdaType)

# Test types.GeneratorType
def gen(a):
    yield a

print(type(gen))
print(types.GeneratorType)
print(type(gen) == types.GeneratorType)

# Test types.BuiltinFunctionType
print(type(abs))
print(types.BuiltinFunctionType)
print(type(abs) == types.BuiltinFunctionType)

# Test types.BuiltinMethodType
print(type(abs))
print(types.BuiltinMethodType)
print(type(abs) == types.BuiltinMethodType)

# Test types.MethodType
class Foo:
    def bar(self):
        pass

print(type(Foo
