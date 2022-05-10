from types import FunctionType
a = (x for x in [1])
print(type(a))
print(a.__next__())
print(a.__next__())

print(type(open))
print(type(abs))
print(type(lambda x: x))
print(type((x for x in range(10))))
print(type(x for x in range(10)))

print(type(FunctionType))
print(type(type))

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
print(obj.y)

print(getattr(obj, 'z', 404))

f = getattr(obj, 'power')
print(f())

