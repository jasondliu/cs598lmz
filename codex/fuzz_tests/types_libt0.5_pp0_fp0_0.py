import types
types.FunctionType

# 判断一个变量是否是字符串
def is_str(s):
    return isinstance(s, basestring)

# 判断一个变量是否是整数
def is_int(s):
    return isinstance(s, int)

# 判断一个变量是否是浮点数
def is_float(s):
    return isinstance(s, float)

# 判断一个变量是否是布尔值
def is_bool(s):
    return isinstance(s, bool)

# 判断一个变量是否是列表
def is_list(s):
    return isinstance(s, list)

# 判断一个变量是否是元组
def is_tuple(s):
    return is
