from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
print(a == b)

# 两个生成器不相等

a = (x for x in [1])
b = (x for x in [1])
print(a == b)

# 不支持复制

def copy_a(a):
    yield from a


def copy_b(b):
    yield from b


a = (x for x in [1])
b = copy_a(a)
c = copy_b(a)
print(a == b)
print(a == c)
print(a is b)
print(a is c)
print(a.gi_code is b.gi_code)
print(a.gi_code is c.gi_code)

# 生成器是一个迭代器，相当于是一个只迭代一次的list，所以支
