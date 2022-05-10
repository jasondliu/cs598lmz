from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)

# 测试生成器的结构
def gen():
    yield 1
    yield 2
    yield 3

for i in gen():
    print(i)

g = gen()
print(g.__next__())
print(g.__next__())
print(g.__next__())

# 测试生成器的结构
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(g.__next__())
print(g.__next__())
print(g.__next__())

# 测试生成器的结构
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g))
print(next(g))
print(next(g))

#
