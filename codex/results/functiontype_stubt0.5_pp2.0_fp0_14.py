from types import FunctionType
a = (x for x in [1])
type(a)

# %%
# 类型判断
def fn():
    pass

type(fn) == types.FunctionType
type(abs) == types.BuiltinFunctionType
type(lambda x: x) == types.LambdaType
type((x for x in range(10))) == types.GeneratorType
isinstance(fn, FunctionType)

# %%
# 使用dir()
dir('ABC')
len('ABC')
'ABC'.__len__()

# %%
# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
hasattr(obj, 'x')
hasattr(obj, 'y')
setattr(obj, 'y',
