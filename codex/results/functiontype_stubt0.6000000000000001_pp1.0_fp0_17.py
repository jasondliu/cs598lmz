from types import FunctionType
a = (x for x in [1])
a

# 不支持带参数的生成器
# a = (x for x in [1] if x > 1)

def foo():
    print('hello')

# 判断一个变量是不是可调用的对象
print(callable(foo))
print(callable(a))
print(callable([]))
print(callable(FunctionType(lambda x: x, {})))

# 可以用来判断一个对象是不是函数
print(isinstance(foo, FunctionType))
