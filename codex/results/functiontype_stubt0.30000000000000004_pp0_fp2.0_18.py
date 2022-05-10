from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__())

# <class 'generator'>
# <class 'method_descriptor'>
# 1

# 上面的代码中，a是一个生成器，a.__next__是生成器的方法，
# a.__next__()是生成器的返回值，这个返回值就是生成器中的元素。

# 如果要获取生成器的返回值，可以使用next()函数：

print(next(a))
# 1

# 如果生成器中没有元素了，那么会
