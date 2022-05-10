from types import FunctionType
a = (x for x in [1])
a.__next__()

isinstance(a, Iterator)

# 迭代器有next方法,也就是说迭代器是可迭代对象
isinstance(a, Iterable)

# function 对象
# 可调用的对象
def f(): pass
isinstance(f, Callable)

# 方法,类方法,静态方法都是可调用的对象

# 方法
# 方法是可调用的对象,它们是函数对象的包装器
# 方法和函数不同的是,方法只有它的类的实例才能调用,

# 方法
