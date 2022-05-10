from types import FunctionType
a = (x for x in [1])
type(a)

b = lambda x: x * x
type(b)

def c(x):
  return x * x
type(c)

print(isinstance(a, Iterator))
print(isinstance(b, FunctionType))
print(isinstance(c, FunctionType))

# 判断是否是可调用的对象
callable(c)
c is callable(c)

# isinstance 和 type的区别
# type() 不会认为子类是一种父类类型

# isinstance判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上
# type 判断的是一个对象的类型，
