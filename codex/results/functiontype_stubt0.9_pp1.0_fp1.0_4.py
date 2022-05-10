from types import FunctionType
a = (x for x in [1])
a.send(0)

a = (1 for i in range(1))
# 定义一个generator，接受一个数值的简单变换
def f(x):
    return x * x
b = map(f, [1,2,3,4,5,6,7,8,9])
print(list(b))


# 洗牌
import random
print('fib')
a = list(range(10))
b = random.sample(a, 9)
print(b)

import random
print('fib')
a = list(range(10))
#print(a)
random.shuffle(a)
print(a)  # [1,7,5,6,8,0,2,9,4,3]


print('fib')
a = list(range(10))
#print(a)
random.shuffle(a)
print(a)  # [1,7,5,6,8,
