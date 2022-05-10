from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(1, int))

# 判断对象是否是可调用对象，如函数、方法、lambda表达式、生成器函数。
# 在Python中，函数、方法、生成器函数、lambda表达式都是可调用对象
print('callable(a)', callable(a))
print('callable(1)', callable(1))
print('callable(f)', callable(f))
print('callable(abs)', callable(abs))
print('callable(print)', callable(print))
print('callable(x)', callable(lambda x: x))
print('callable(len)', callable(len))


# 判
