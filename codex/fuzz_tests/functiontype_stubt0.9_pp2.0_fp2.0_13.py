from types import FunctionType
a = (x for x in [1])
print(type(1))
print(type('str'))
print(type([1,2,3]))
print(type({1,3,3}))
print(type({'name':'xunxun'}))

# 基类  继承object
print(int.__bases__)
print(str.__bases__)
print(list.__bases__)
print(dict.__bases__)
