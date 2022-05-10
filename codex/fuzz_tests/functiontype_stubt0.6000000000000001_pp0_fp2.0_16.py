from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(abs))
print(type(lambda x: x))
print(type((x for x in range(10))))

a = abs
print(type(a))
print(a(-1))

print(isinstance(a, FunctionType))
print(isinstance(a, abs))

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

setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))

print(getattr(obj, 'z', 404))

f = getattr(obj, 'power')
print(f)
print(f())
