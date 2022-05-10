from types import FunctionType
list(FunctionType(lambda x:x+1, globals()) for x in range(3))  # [1, 2, 3]

from functools import reduce
from operator import add
reduce(add, map(lambda x:x+1, range(3)))  # 6
reduce(add, [x+1 for x in range(3)])  # 6

from operator import mul
reduce(mul, range(1, 4))  # 6
reduce(mul, [x+1 for x in range(3)])  # 6

# 对于map还有另外一个比较有趣的地方，就是它的每一个元素，可以是一个tuple，那么这个tuple的元素就会被当作两个参数传入
from itertools import filterfalse
filterfalse(lambda x:x>0,
