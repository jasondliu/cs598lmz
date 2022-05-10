import types
types.FunctionType

# 判断一个变量是否是函数
def is_function(var):
    return isinstance(var, types.FunctionType)

# 判断一个变量是否是字符串
def is_string(var):
    return isinstance(var, types.StringType)

# 判断一个变量是否是类型
def is_type(var):
    return isinstance(var, types.TypeType)

# 判断一个变量是否是模块
def is_module(var):
    return isinstance(var, types.ModuleType)

# 判断一个变量是否是模块
def is_list(var):
    return isinstance(var, types.ListType)

# 判断一个变量是否是字典

