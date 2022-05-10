from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(abs))
print(type(lambda x: x))

# 总结：
# 判断一个对象的类型，可以用type()函数
# 判断的类型可以用isinstance()函数
# 判断一个对象是否是函数，可以用types模块中定义的常量

# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
# 能用type()判断的基本类型也
