from types import FunctionType
a = (x for x in [1])
b = list(a)
c = type(a)
print(b)
print(c)
print(type(type(a)))

'''
[1]
<class 'generator'>
<class 'type'>

# 可以用type判断元祖中变量的类型
l = [1,2,3,4]
t = (1,'ds',[],FunctionType(print))
for i in t:
    print(type(i))

'''

# 方法二
import types
print(type(a) == types.GeneratorType)
print(type(a) == types.GeneratorType)

# 方法三
from collections import Iterator
print(isinstance(a,Iterator))
print(isinstance(b,Iterator))

# 可以用isinstance判断变量是否是一个可迭代的对象
