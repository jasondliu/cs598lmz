import types
types.ClassType

# 判断一个对象是否是函数
def fn():
    pass

type(fn) == types.FunctionType
type(abs) == types.BuiltinFunctionType
type(lambda x: x) == types.LambdaType
type((x for x in range(10))) == types.GeneratorType

# 使用isinstance()
isinstance([1, 2, 3], (list, tuple))
isinstance((1, 2, 3), (list, tuple))

# 使用dir()
dir('ABC')
len('ABC')
'ABC'.__len__()

# 类型转换
int('123')
int(12.34)
float('12.34')
str(1.23)
