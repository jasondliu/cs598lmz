from types import FunctionType
a = (x for x in [1])
print(type(a))

def fn():
    pass
print(type(fn))
print(type(fn) == FunctionType)

print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)
print(type(x for x in range(10)) == types.GeneratorType)

print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

print(dir('ABC'))

class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x'))
print(obj.x)

