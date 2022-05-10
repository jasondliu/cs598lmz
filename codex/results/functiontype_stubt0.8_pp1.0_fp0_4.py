from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, Iterator))
# 注意可迭代对象有两个类型：迭代器和生成器，迭代器是可以迭代的对象，生成器是可迭代对象的生成器，
# 可迭代对象是生成器
print(iter(a))
print(iter([]))

# import types
a = (x for x in [3])
print(type(a))
print("判断a是不是可迭代对象")
print(isinstance(a, Iterator))
print("判断a是不是生成器")
print(isinstance(a, GeneratorType))
print("判断a是不是可
