import types
types.FunctionType

# 判断是否是函数
def fn():
    pass

type(fn) == types.FunctionType

# 判断是否是类型
type(abs) == types.BuiltinFunctionType

# 判断是否是模块
type(math) == types.ModuleType

# 判断是否是方法
type(abs) == types.MethodType

# 使用dir()
