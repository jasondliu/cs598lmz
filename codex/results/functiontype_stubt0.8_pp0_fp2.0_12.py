from types import FunctionType
a = (x for x in [1])

# 判断一个对象是否是可调用对象
callable(a)

import string
def bar():
    return 1, 2, 3


string.join(['a', 'b'], '-')

filter(lambda x: x % 2, [1,2,3])

map(lambda x,y: x + y, [1,2,3], [4,5,6])

reduce(lambda x,y: x+y, [1,2,3])

# 分组排序
import itertools
a = [1,3,2,1,3,3,3,3,2,2,2,2,2,1,1,2,2,1,1,2,2,2]
map(lambda x: list(x[1]), itertools.groupby(a))

# 判断两个值是否数值相等
x =
