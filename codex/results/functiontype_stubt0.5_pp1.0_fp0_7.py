from types import FunctionType
a = (x for x in [1])
type(a)

#%%
import types
def fn():
    pass
type(fn) == types.FunctionType
type(abs) == types.BuiltinFunctionType
type(lambda x: x) == types.LambdaType
type((x for x in range(10))) == types.GeneratorType

#%%
isinstance([1, 2, 3], (list, tuple))
isinstance((1, 2, 3), (list, tuple))

#%%
# 获取对象信息
# 要获取一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list

print(dir("ABC"))

#%%
# 实例属性和类属性
# 给实例绑定
