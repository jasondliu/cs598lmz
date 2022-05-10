import types
types.FunctionType

# 判断是否是函数
def fn():
    pass

type(fn) == types.FunctionType
type(abs) == types.BuiltinFunctionType
type(lambda x: x) == types.LambdaType
type((x for x in range(10))) == types.GeneratorType

# 判断是否是某些类型中的一种
isinstance([1, 2, 3], (list, tuple))
isinstance((1, 2, 3), (list, tuple))

# 判断是否是某个类型的实例
isinstance('abc', str)
isinstance(123, int)
isinstance(b'a', bytes)

# 判断是否是某个类型
type('abc') == str
type(123) == int
type(b'a') == bytes

# 判断是否是某
