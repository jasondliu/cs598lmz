from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(1))
print(type(int))
print(type(abs))
print(type(a) == types.GeneratorType)
print(type(a) == FunctionType)
print(type(lambda x: x) == types.LambdaType)

#判断一个对象是否是函数
def rf():
    pass
print(type(rf) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

#如果要获得一个对象的所有属性和方法，可以使用dir()函数
print(dir('ABC'))

print(len('ABC'))
print('ABC'.__len__())

