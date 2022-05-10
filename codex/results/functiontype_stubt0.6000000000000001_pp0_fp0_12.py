from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 迭代器
print(isinstance(a, Iterator))

# 一切都可以迭代
print(hasattr(a, '__iter__'))
print(hasattr([], '__iter__'))
print(hasattr('abc', '__iter__'))
print(hasattr(123, '__iter__'))
print(hasattr(None, '__iter__'))

# 可以使用next方法获取下一个元素
print(hasattr(a, '__next__'))
print(hasattr([], '__next__'))
print(hasattr('abc', '__next__'))
print(hasattr(123, '__next__'))
print(hasattr(None, '__next__'))

# iter函数返回一个迭代器
