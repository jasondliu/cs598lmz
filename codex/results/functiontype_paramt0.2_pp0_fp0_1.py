from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda').__code__.co_varnames)

# ['__annotations__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']

# 但是，如果我们把这个函数赋值给一个变量，再获取它的属性，就没有 co_varnames 了：

fn = lambda: None
list(fn.__code__.co_varnames)

# []

# 这是因为 Python 解释器会把 lambda 表达式预先解析成一个标准的函数对象。

#
