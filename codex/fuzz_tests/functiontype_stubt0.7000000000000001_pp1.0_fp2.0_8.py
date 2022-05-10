from types import FunctionType
a = (x for x in [1])
b = a.__iter__()
print(a is b)
print(type(b.__iter__))
print(isinstance(b.__iter__, FunctionType))
print(callable(b.__iter__))
print(type(b.__iter__()))
print(isinstance(b.__iter__(), Iterator))
print(type(b.__next__))
print(isinstance(b.__next__, FunctionType))
print(callable(b.__next__))
print(type(b.__next__()))
print(isinstance(b.__next__(), int))
print(b.__next__.__self__ is a)
print(a.__next__.__self__ is a)
print(a.__next__() is a.__next__())

# 下面的例子为了说明，不能只看返回值，也必须要看是否被调用
