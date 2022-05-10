import types
types.FunctionType

# 判断变量是否是函数
def fn():
    pass

type(fn) == types.FunctionType
type(abs) == types.BuiltinFunctionType
type(lambda x: x) == types.LambdaType
type((x for x in range(10))) == types.GeneratorType

# 判断变量是否是某些类型中的一种
isinstance([1, 2, 3], (list, tuple))
isinstance((1, 2, 3), (list, tuple))

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
dir('ABC')
len('ABC')
'ABC'.__len__()

# 如果
