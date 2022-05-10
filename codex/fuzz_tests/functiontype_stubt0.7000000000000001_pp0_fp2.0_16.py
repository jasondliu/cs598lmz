from types import FunctionType
a = (x for x in [1])
print(type(a))
# <class 'generator'>

b = (x for x in [1]).__iter__()
print(type(b))
# <class 'generator'>

c = (x for x in [1]).__next__()
print(type(c))
# <class 'int'>

d = (x for x in [1]).close
print(type(d))
# <class 'method'>

e = (x for x in [1]).send
print(type(e))
# <class 'method'>

f = (x for x in [1]).throw
print(type(f))
# <class 'method'>


# 生成器表达式对象有个 gi_running属性，标记生成器对象是否处在运行状态
a = (x for x in [1])
print(a.gi_running)
# False

#
