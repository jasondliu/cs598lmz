from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, FunctionType))

# 生成器是一个迭代器
# 迭代器是一个可以被next()函数调用并不断返回下一个值的对象
# 生成器是一个返回迭代器的函数，只能用于迭代操作
# 迭代器可以被next()函数调用并不断返回下一个值
# 生成器可以被next()函数调用并不断返回下一个值
# 迭代器可以表示一个无限
