from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 可以看到，生成器（生成器函数或者生成器表达式）不是一个普通函数，而是一个特殊的迭代器。
# 可以直接用for循环迭代，而不需要额外的函数，这也是生成器的一个特点。
# 另一个特点是，生成器的函数中不能使用return语句，因为生成器的函数的返回值是一
