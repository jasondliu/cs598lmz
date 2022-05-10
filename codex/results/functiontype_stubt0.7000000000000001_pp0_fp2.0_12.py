from types import FunctionType
a = (x for x in [1])
next(a)

def b():
    pass

type(b) == FunctionType
type(b) == types.FunctionType

type(b) == types.GeneratorType

import sys
a = (x for x in range(10000))
sys.getsizeof(a)

sum(a)

a = [x for x in range(10000)]
sys.getsizeof(a)

sum(a)

#消耗时间
import time
start = time.clock()

a = (x for x in range(1000000))
sys.getsizeof(a)
sum(a)

print(time.clock() - start, 's')

start = time.clock()

a = [x for x in range(1000000)]
sys.getsizeof(a)
sum(a)

print(time.clock() - start, 's')

# 生成器的优势
def fib(n):
    a, b = 0, 1
    for i in range(
