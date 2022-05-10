from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)
print(a.__next__())

# 判断一个对象是否是函数
print(callable(a))
print(callable(a.__next__))

# 生成器
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)
print(a.__next__())

# 判断一个对象是否是函数
print(callable(a))
print(callable(a.__next__))

import random
def rand_num(n,m):
    while True:
        yield random.randint(n,m)

for i in rand_num(1,100):
    print(i)
    if i == 88:
        break
