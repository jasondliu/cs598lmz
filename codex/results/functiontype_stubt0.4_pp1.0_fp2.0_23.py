from types import FunctionType
a = (x for x in [1])
print(type(a))

# 函数对象
def func():
    pass
print(type(func))
print(type(abs))
print(type(lambda x: x))
print(type((x for x in range(10))))
print(type(x for x in range(10)))

# 判断一个对象是否是函数
print(callable(func))
print(callable(abs))
print(callable(lambda x: x))
print(callable((x for x in range(10))))
print(callable(x for x in range(10)))
print(callable(a))

# 使用__slots__
# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
