import types
# Test types.FunctionType
def func(x):
    return x

print(type(func) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.MethodType
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

a = Animal()
d = Dog()
c = Cat()

print(type(a.run) == types.MethodType)
print(type(d.run) == types.MethodType)
print(type(c.run) == types.MethodType)

# Test types.UnboundMethodType
print(type(Animal.run) == types.UnboundMethodType)
print(type(Dog.run) == types.Un
