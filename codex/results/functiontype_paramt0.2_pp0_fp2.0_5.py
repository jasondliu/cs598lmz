from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['__module__', '__qualname__', '__annotations__', '__kwdefaults__', '__defaults__', '__closure__', '__code__', '__globals__', '__dict__', '__doc__', '__name__', '__defaults__', '__code__', '__globals__', '__dict__']

# 从上面的结果可以看出，一个函数的属性有很多，其中有一些是内置的，有一些是用户自定义的。
# 其中，__code__属性是用来存放函数的字节码对象的，这个对象有一个co
