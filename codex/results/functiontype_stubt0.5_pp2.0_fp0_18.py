from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
print(type(a), type(b))
print(type(a) == GeneratorType)
print(type(b) == ListType)
print(type(b) == FunctionType)
print(type(abs) == FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == FunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in [1]) == types.GeneratorType)

# 判断class的类型
print(type(int) == type(str) == types.TypeType)
print(type(int) == types.TypeType)
print(type(int) == type)

# 使用dir()
print(dir('abc'))
print(len('abc'))
print('abc'.__len__())

class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):

