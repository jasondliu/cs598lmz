from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(lambda x: x + 1))
print(type(map))
print(type(a.__next__))  # 可以看到__next__是一个函数
print(type(a.__next__()) is int)  # __next__返回的结果也是int类型
print(type(set))
print(type(int))
print(type(object))

# 类型判断是通过isinstance()函数实现的
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

# dir()函数可以查看一个对象有哪些方法和属性
print(dir(a))

# 把list, dict, str等Iterable变成Iterator可以使
