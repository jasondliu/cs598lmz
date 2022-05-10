from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(abs))
print(type(lambda x: x))
print(type((x for x in [1])))
print(type(FunctionType))

print(isinstance(a, GeneratorType))
print(isinstance(abs, FunctionType))
print(isinstance(lambda x: x, FunctionType))

print(dir('ABC'))

print(len('ABC'))
print('ABC'.__len__())

print('ABC'.lower())

class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)

print(getattr(obj, 'z', 404))


