from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

print(isinstance(abs, FunctionType))

print(type(123))
print(type(lambda x: x))
print(type(x for x in range(10)))

print(type(abs) == types.BuiltinFunctionType)
print(type(a) == types.GeneratorType)

print(dir('ABC'))

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
print(obj.y)

print(getattr(obj, 'z', 404))

f = getattr(obj, 'power')
print(f)
print(f())

def readImage(fp):
   
