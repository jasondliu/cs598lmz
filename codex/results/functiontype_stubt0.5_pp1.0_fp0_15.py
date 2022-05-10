from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 自定义生成器
def my_generator():
    for i in range(10):
        yield i

print(my_generator())
print(next(my_generator()))
