from types import FunctionType
a = (x for x in [1])
b = [1]
c = 1
d = FunctionType
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# isinstance
print(isinstance(a, GeneratorType))
print(isinstance(b, list))
print(isinstance(c, int))
print(isinstance(d, FunctionType))

# dir
print(dir('abc'))

# getattr
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
print(getattr(obj, 'z', 404))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn())


