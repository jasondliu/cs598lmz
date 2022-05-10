from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, FunctionType))
# 生成器函数
def gen_func():
    yield 1
    yield 2
    yield 3
a = gen_func()
print(isinstance(a, GeneratorType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, FunctionType))
# 可迭代对象
a = [1, 2, 3]
print(isinstance(a, GeneratorType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, FunctionType))
# 迭代器
a = iter([1, 2, 3])
print(isinstance(a, GeneratorType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a,
