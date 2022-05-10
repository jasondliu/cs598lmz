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

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    pass

def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
d = Dog()
c = Cat()

print(type(run_twice) == types.FunctionType)
print(type(run_twice) == types.MethodType)
print(type(a.run) == types.MethodType)
print(type(d.run) == types.MethodType)
print(type(c.
