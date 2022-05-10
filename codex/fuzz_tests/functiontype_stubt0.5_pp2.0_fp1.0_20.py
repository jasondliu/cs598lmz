from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(str))
print(type(FunctionType))
print(type(abs))
print(type(lambda x: x))
print(type(x for x in range(10)))
print(type(123))

print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))

print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

print(dir('ABC'))

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
print(setattr(obj, 'y', 19))
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print
