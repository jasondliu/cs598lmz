from types import FunctionType
a = (x for x in [1])
#print type(a)
# 判断是否是可迭代对象
from collections import Iterable
#isinstance(a, Iterable)
# 判断是否是迭代器
from collections import Iterator
isinstance(a, Iterator)


# 列表生成式
str = 'ABCD'
#print [i+'A' for i in str]
# 生成器
g = (i+'A' for i in str)
#for i in g:
#    print i
# 迭代器
it = iter(g)
for i in it:
    print i

# 函数
# 参数不确定
def func1(*args):
    print args
func1('a', 'b')
# 参数的 key=value形式
def func2(**keyargs):
    print keyargs
func2(a=1, b='2')

