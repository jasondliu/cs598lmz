import types
types.FunctionType

# 判断是否是函数
def fn():
    pass

type(fn) == types.FunctionType

# 判断是否是类
type(fn) == types.ClassType

# 判断是否是模块
type(fn) == types.ModuleType

# 判断是否是字符串
type(fn) == types.StringType

# 判断是否是Unicode字符串
type(fn) == types.UnicodeType

# 判断是否是元组
type(fn) == types.TupleType

# 判断是否是列表
type(fn) == types.ListType

# 判断是否是字典
type(fn) == types.DictType

# 判断是否是整数
type(fn) ==
