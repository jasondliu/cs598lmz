from types import FunctionType
a = (x for x in [1])
b = [1,2,3]
c = 'abc'
d = {1,2,3}
e = {'a':1,'b':2}
f = FunctionType
g = type
h = object
print(type(a),type(b),type(c),type(d),type(e),type(f),type(g),type(h),sep='\n')

#判断一个对象是否是函数
#可以用types模块中定义的常量去判断
import types
def fn():
    pass
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x:x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

#判断一个对象是否是可调用对象

