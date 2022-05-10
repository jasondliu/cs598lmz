import types
types.FunctionType

# 判断一个对象是否是函数
def fn():
    pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

# 使用isinstance()
print(isinstance([1,2,3],(list,tuple)))
print(isinstance((1,2,3),(list,tuple)))

# dir()
print(dir('ABC'))

# len()
print(len('ABC'))
print('ABC'.__len__())

# getattr()、setattr()以及hasattr()
class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x

obj=MyObject()

