from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 在 Python 2 中，生成器是一个类型
# 在 Python 3 中，生成器是一个函数

# 生成器是一种特殊的迭代器，可以被 next() 函数调用并不断返回下一个值，直到最后抛出 StopIteration 错误表示无法继续返回下一个值了。
# 可以被 next() 函数调用并不断返回下一个值，直到最后抛出 StopIter
