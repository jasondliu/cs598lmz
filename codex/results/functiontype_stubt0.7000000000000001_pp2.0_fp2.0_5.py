from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

print(isinstance(abs, FunctionType))
print(type(abs)==FunctionType)

print(dir('ABC'))

print(len('ABC'))

print('ABC'.__len__())

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
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)

print(getattr(obj, 'z', 404))

f = getattr(obj, 'power')
print(f())

print(
