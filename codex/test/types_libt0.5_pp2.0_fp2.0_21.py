import types
types.FunctionType

# 判断是否是某个类型，不是就报错
def fn(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    return x

fn('a')

# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
# 能用type()判断的基本类型也可以用isinstance()判断：

a = Animal()
isinstance(a, Animal)
isinstance(a, Dog)
