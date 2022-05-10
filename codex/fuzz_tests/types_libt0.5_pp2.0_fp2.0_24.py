import types
types.FunctionType

# 判断是否是某类型
isinstance(abs, types.BuiltinFunctionType)

# 判断是否是某类型中的一种
isinstance([1, 2, 3], (list, tuple))

# 获取对象的类型
type(123)
type('str')
type(None)

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
dir('ABC')

# 仅仅把
