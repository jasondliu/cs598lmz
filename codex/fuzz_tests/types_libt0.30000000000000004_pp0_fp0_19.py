import types
types.ClassType

# 对于类型的判断，可以使用isinstance()函数
# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
# 如果继承关系有二义性，建议不要使用isinstance()，而使用直接判断类型

# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
#
