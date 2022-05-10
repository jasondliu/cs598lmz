from types import FunctionType
list(FunctionType(lambda x: x*x, {})(i) for i in range(10))

# 2.3
from functools import reduce
def sum(x, y):
    return x + y
print(reduce(sum, [1, 2, 3, 4, 5]))

# 2.4
import math
def quadratic(a, b, c):
    delta = b * b - 4 * a * c
    if delta < 0:
        print('此二次方程无解')
        return None
    elif delta == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2

print(quadratic(1, 2, 1))

# 2.5
def power(x, n):
    s = 1
    while n > 0:
        n =
