from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

print('-------------------')

# 生成器函数
def gen():
    yield 1
    yield 2
    yield 3

print(gen())
print(isinstance(gen(), GeneratorType))
print(isinstance(gen(), FunctionType))
print(isinstance(gen(), Iterator))
print(isinstance(gen(), Iterable))
print(isinstance(gen(), Iterator))
print(isinstance(gen(), Iterable))

print('-------------------')

# 生成器表达式
b = (x for x in [1, 2, 3])
print(b)
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))
print(isinstance
