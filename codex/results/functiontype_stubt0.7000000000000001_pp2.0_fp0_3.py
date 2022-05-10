from types import FunctionType
a = (x for x in [1])
isinstance(a,types.GeneratorType)

type(a) is types.GeneratorType

isinstance(a, types.GeneratorType)

# 进行类型检查时，与 type() 完全相同，但是 isinstance() 会认为子类是一种父类类型，
# 比如，a = [] 是 list 类型，而 type() 不认为它是 tuple 类型，所以，进行类型判断时，
# 可以使用 isinstance() 来代替 type()：

#可以判断一个变量是否是某些类型中的一
