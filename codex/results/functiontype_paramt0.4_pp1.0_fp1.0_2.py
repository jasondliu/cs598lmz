from types import FunctionType
list(FunctionType(lambda: 0, {}, '', (), None).__code__.co_varnames)

# ['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']

# 使用__annotations__属性来查看函数的参数类型和返回值类型

# def f(a: int, b: int) -> int:
#     return a + b
#
#
# print(f.__annotations__)

# {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}


# 函数的__closure__属性
# 函数的__closure__属性是一个元组，每个
