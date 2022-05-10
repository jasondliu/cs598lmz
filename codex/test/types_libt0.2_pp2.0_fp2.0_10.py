import types
types.FunctionType

# 判断是否是函数
def fn():
    pass

type(fn) == types.FunctionType

# 判断是否是类
class Animal(object):
    pass

type(Animal) == types.ClassType

# 判断是否是模块
import sys
type(sys) == types.ModuleType

# 判断是否是字符串
type('abc') == types.StringType

# 判断是否是列表
type([]) == types.ListType

# 判断是否是字典
type({}) == types.DictType

# 判断是否是元组
type(()) == types.TupleType

# 判断是否是整型
type(1) == types.IntType

# 判断是否是浮点
