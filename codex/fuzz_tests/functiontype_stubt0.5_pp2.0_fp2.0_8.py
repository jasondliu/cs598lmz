from types import FunctionType
a = (x for x in [1])
type(a)

# 如果一个变量指向函数，也可以用type()判断：
def fn():
    pass

type(fn) == types.FunctionType
type(abs) == types.BuiltinFunctionType
type(lambda x: x) == types.LambdaType
type((x for x in range(10))) == types.GeneratorType

# 使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
# 我们回顾上次的例子，如果继承关系是：
# object -> Animal -> Dog -> Husky
#
