from types import FunctionType
list(FunctionType(lambda: None).__code__.co_varnames)

# ['__qualname__', '__annotations__', '__closure__', '__code__', '__defaults__', '__globals__', '__kwdefaults__', '__name__', '__dict__', '__doc__', '__module__', '__weakref__']

# 参数类型检查
def my_add(x: int, y: int) -> int:
    return x + y

# my_add(1, 2)
# my_add(1, '2')

# 可选参数
def my_add_default(x: int, y: int, z: int = 0) -> int:
    return x + y + z

# my_add_default(1, 2)
# my_add_default(1, 2, 3)

# 可变参数
def my_add_variable(*args: int) -> int:
    return sum(args
