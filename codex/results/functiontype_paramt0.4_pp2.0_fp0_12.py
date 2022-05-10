from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__))

# 可以通过__code__属性获取函数的code对象
# 可以通过__globals__属性获取函数的全局变量
# 可以通过__name__属性获取函数的名字
# 可以通过__defaults__属性获取函数的默认参数
# 可以通过__closure__属性获取函数的闭包
# 可以通过__kwdefaults__属性获取函数的默认关
