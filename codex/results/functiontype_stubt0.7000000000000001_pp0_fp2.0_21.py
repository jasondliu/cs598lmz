from types import FunctionType
a = (x for x in [1])
print(isinstance(a, FunctionType))
print(isinstance(a, (int, FunctionType)))

# 如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types

def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):
    @property
    def width(self):
        return self._width
   
