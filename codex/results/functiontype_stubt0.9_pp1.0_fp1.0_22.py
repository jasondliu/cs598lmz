from types import FunctionType
a = (x for x in [1])
print(a)  # <generator object <genexpr> at 0x7fae1c72e1a8>

b = [x for x in [1]]
print(b)  # [1]

print(type(a))  # <class 'generator'>
print(type(b))  # <class 'list'>

print(isinstance(a, FunctionType))  # False
print(isinstance(a, GeneratorType))  # True
print(isinstance(b, FunctionType))  # False
print(isinstance(b, GeneratorType))  # False

# 如果要一步步获取生成的值，可以通过 next() 函数获得 generator 的下一个返回值：
a = (x for x in [1, 2])
print(next(a))  # 1
print(next(a))  # 2
# print(next(a))  # StopIteration

