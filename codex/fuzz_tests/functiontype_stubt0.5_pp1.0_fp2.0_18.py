from types import FunctionType
a = (x for x in [1])
print(a)
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
print(isinstance(a, Iterator))

# 生成器函数
def gen():
    for i in range(3):
        yield i
print(isinstance(gen(), GeneratorType))
print(isinstance(gen(), FunctionType))

# 列表推导式
a = [x for x in range(3)]
print(a)
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 字典推导式
a = {x:x for x in range(3)}
print(a)
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 集合推导式
a = {x
