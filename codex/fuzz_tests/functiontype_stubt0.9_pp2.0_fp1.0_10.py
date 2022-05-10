from types import FunctionType
a = (x for x in [1])
print(isinstance(a, FunctionType))
print(isinstance(a, GeneratorType))



# 一个生成器函数与一个常规函数之间的区别是生成器函数中有一个或多个yield语句
a = (x for x in range(10))
print(type(a), a)
b = 10
print(type(b), b)
# 我们可以通过help(a)来查看生成器对象的属性和方法，
help(a)
