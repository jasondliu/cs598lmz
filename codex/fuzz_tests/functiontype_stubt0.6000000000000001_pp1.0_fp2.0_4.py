from types import FunctionType
a = (x for x in [1])
print(a)
print(isinstance(a, FunctionType))
print(isinstance(a, GeneratorType))
print(isinstance(a, IteratorType))

# 迭代器
# 可迭代对象
# 迭代器
# 生成器

# 可迭代对象
# 可以通过iter()函数获得一个迭代器
# 迭代器
# 可以通过next()函数获得下一个值

# 生成器
# 生成器是迭代器
# 生成器是可迭代对象
# 可以把列表生成式的[]改成()，就创建了一
