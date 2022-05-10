from types import FunctionType
a = (x for x in [1])
print(a, type(a))
b = (x for x in [1])
print(a == b)
print(a is b)
c = 1
print(a == c)  # 生成器是可迭代对象，类型不一样，肯定不等
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))  # 生成器没有 func_code 属性
print("==================")
l = [1, 2, 3]
print(isinstance(l, GeneratorType))
print(isinstance(l, FunctionType))
print(isinstance(l, Iterator))
print(isinstance(l, Iterable))
