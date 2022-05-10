from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x:x))
print(type(abs))
print(type(a) == GeneratorType)
print(type(lambda x:x) == FunctionType)
print(type(abs) == BuiltinFunctionType)
print(type(lambda x:x) == types.LambdaType)
print(type(abs) == types.BuiltinFunctionType)

print(isinstance(a, GeneratorType))
print(isinstance(lambda x:x, FunctionType))
print(isinstance(abs, BuiltinFunctionType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, GeneratorType))

print(dir('ABC'))
print('ABC'.__len__())

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x'))
print(obj.x)
print
