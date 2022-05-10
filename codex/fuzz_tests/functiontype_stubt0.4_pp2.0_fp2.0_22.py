from types import FunctionType
a = (x for x in [1])
print(type(a))

print(type(lambda x: x))
print(type(abs))
print(type(a) == FunctionType)

print(type(lambda x: x) == types.GeneratorType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

print(isinstance(b'a', bytes))

print(dir('ABC'))

print(len('ABC'))
print('ABC'.__len__())

class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))

print('ABC'.lower())

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x'))
print(obj
