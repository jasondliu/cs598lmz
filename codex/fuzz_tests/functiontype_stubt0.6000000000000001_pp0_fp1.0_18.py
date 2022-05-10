from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)

print(isinstance(abs, FunctionType))
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in [1]))==types.GeneratorType)
print(isinstance((x for x in [1]), types.GeneratorType))
print(isinstance((x for x in [1]), Iterable))

print(dir('abc'))

class MyObject(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()
print(hasattr(obj, 'x')) # 有属性'x'吗？
print(obj.x)
print(hasattr(obj, 'y')) # 有属性'y'吗？
setattr(obj, 'y', 19) # 设
