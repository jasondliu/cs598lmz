from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x))
print(type(1))
print(type(a) == GeneratorType)
print(type(lambda x: x) == FunctionType)
print(type(1) == int)
print(isinstance(a, GeneratorType))
print(isinstance(lambda x: x, FunctionType))
print(isinstance(1, int))
print(type(1) is int)

# 定义
class Hello(object):
    def hello(self, name = 'world'):
        print('Hello %s.'%name)

# 实例化
h = Hello()
print(type(Hello))
print(type(h))
print(h.__class__)

# 方法
from types import MethodType
def fn(self, name = 'world'):
    print('Hello %s.'%name)

h.hello = MethodType(fn, h)
h.hello()

# 绑定到类上
Hello.hello =
