from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__iter__))
print(type(a.__next__) == type(a.__iter__))
print(type(a.__next__) == FunctionType)
print(type(a.__iter__) == FunctionType)
print(type(a.__next__) == type(a.__iter__) == FunctionType)

# 上面的例子中，我们看到了生成器的几个方法，__next__, __iter__, 但是我们注意到，这两个方法的类型都是函数类型，
# 也就是说，__next__方法和__iter__方法，都是函数，而不是方法，
