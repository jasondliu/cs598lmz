from types import FunctionType
a = (x for x in [1])
b = (x for x in [1, 2, 3])

print("a: {0}, b: {1}".format(a, b))
print("a: {0}, b: {1}".format(type(a), type(b)))
print(a.__next__())
print(next(b))
for n in b:
    print(n)

print(type(a) is generator)
print(isinstance(a, FunctionType))

print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))

# Iterable
print(isinstance(a, Iterable))
print(isinstance(b, Iterable))

# Iterator
print(isinstance(a, Iterator))
print(isinstance(b, Iterator))

# 如果一个对象定义了__iter__方法，那么它不仅可以用于for循环，也可以用
