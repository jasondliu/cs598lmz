from types import FunctionType
list(FunctionType(lambda x: x*x, globals(), "square")(3))
#[0]

#lambda表达式只能有一个表达式，不用写return，返回值就是该表达式的结果。
#return None

f = lambda x: x * x
print(f)
print(f(5))

#匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
#函数对象有一个__name__属性，可以拿到函数的名字
print(f.__name__)
