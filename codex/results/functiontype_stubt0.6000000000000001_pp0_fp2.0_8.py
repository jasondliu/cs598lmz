from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(FunctionType))
print(type(a) == FunctionType)
print(type(a) is FunctionType)

print(isinstance(a, FunctionType))
print(isinstance(a, (FunctionType,)))
print(isinstance(a, (FunctionType, type(a))))
print(a.__class__)

# 类型判断
print(type(a) == type(FunctionType))
print(type(a) is type(FunctionType))

print("=" * 40)
print(type(1))
print(type(int))


# 可以动态创建类
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)


h = Hello()
print(type(Hello))
print(type(h))
print(type(Hello) == type(h))
print(type(Hello) is type(h))

# 动态
