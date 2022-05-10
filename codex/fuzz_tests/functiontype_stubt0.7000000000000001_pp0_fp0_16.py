from types import FunctionType
a = (x for x in [1])
b = (x for x in [1,2])
c = {}
print(type(a))
print(type(b))
print(type(c))

print(type(lambda x:x) == FunctionType)
print(type(lambda x:x) == types.FunctionType)

print(type(abs))
print(type(a))
print(type(b))
print(type(c))

print(isinstance([1,2,3], (list, tuple)))

print(dir('ABC'))
print('ABC'.__len__())
print('ABC'.lower())

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(getattr(obj,
