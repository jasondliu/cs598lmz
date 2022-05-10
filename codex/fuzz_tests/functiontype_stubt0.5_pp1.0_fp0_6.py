from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
print(type(a), type(b))
print(isinstance(a, GeneratorType), isinstance(b, GeneratorType))
print(isinstance(a, FunctionType), isinstance(b, FunctionType))
print(isinstance(a, list), isinstance(b, list))

# 迭代器
# 实现了__iter__方法的对象
# 实现了__next__方法的对象
# 实现了__getitem__方法的对象
print(isinstance(a, Iterator))
print(isinstance(b, Iterator))
print(isinstance(b, Iterator))
print(isinstance(b, Iterator))

# 可迭代对象
# 实现了__iter__方法的对象
# 实现了__getitem__方法的对
