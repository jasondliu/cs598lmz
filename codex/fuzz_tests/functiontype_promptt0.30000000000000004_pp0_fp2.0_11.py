import types
# Test types.FunctionType
def func(x):
    return x

print(type(func))
print(type(func) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.MethodType
class Animal(object):
    def run(self):
        print('Animal is running...')

a = Animal()
print(type(a.run) == types.MethodType)

# Test types.UnboundMethodType
def run_twice(animal):
    animal.run()
    animal.run()

print(type(run_twice) == types.FunctionType)
print(type(run_twice.__func__) == types.FunctionType)
print(type(run_twice.__func__.__get__(a, Animal)) == types.MethodType)

# Test types.BuiltinMethodType
print(type(abs) == types.BuiltinFunctionType
