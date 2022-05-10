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
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
dir('
