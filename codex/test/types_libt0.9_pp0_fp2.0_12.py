import types
types.FileType

# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
# 我们回顾上次的例子，如果继承关系是：
#
# object --- Animal ---> Dog ---> Husky
#
# 那么，isinstance()就可以告诉我们，一个对象是否是某种类型。先创建3种类型的对象：
a = Animal()
d = Dog()
h = Husky()
print(isinstance(h, Husky))
