import types
# Test types.FunctionType
def func():
    pass

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
class Dog(Animal):
    def run(self):
        print('Dog is running...')

print(type(Dog.run) == types.UnboundMethodType)

# Test types.BuiltinMethodType
print(type(str.lower) == types.BuiltinMethodType)

# Test types.ModuleType
print(type(urllib) == types.ModuleType)

# Test types.TypeType
print(type(int) == types.TypeType)

# Test types.Traceback
