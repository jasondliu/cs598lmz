from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
if isinstance(a, Iterable):
    print("a是迭代器类型")
else:
    print("a不是迭代器类型")

b = (x for x in [1])
print(b)
print(type(b))
if isinstance(b, Iterable):
    print("b是迭代器类型")
else:
    print("b不是迭代器类型")
