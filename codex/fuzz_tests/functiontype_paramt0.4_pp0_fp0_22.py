from types import FunctionType
list(FunctionType(None, None, None, None, None).__dict__.keys())

# ['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__',
# '__globals__', '__kwdefaults__', '__name__', '__qualname__']

# При создании класса переменные, определенные в нем, попадают в пространство имен класса и в пространство имен объекта.
# При создании функции переменные, определенные
