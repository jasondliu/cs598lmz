import types
types.FunctionType

# 用偏函数模块functools把这个操作简单化
import functools
int2 = functools.partial(int,base=2)
int2('10010')


# 正则表达式
import re
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
re_telephone.match('010-12345').groups()
re_telephone.match('010-8086').groups()
