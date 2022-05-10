import types
types.FunctionType

# 判断一个对象是否是函数
def fn():
    pass

type(fn) == types.FunctionType

# 判断一个对象是否是generator
def gen():
    yield 1

type(gen) == types.GeneratorType

# 判断一个对象是否是某个类型
isinstance([1, 2, 3], (list, tuple))

# 判断一个对象是否是某个类的实例
isinstance(gen, types.GeneratorType)

# 判断一个对象是否是某个类型或者某个类的实例
isinstance(gen, (types.GeneratorType, types.FunctionType))

# 判断一个
