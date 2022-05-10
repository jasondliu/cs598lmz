import types
types.ClassType

# 因此，在Python中，除了真正的类外，还可以用type()函数创建出类来，也就是：通过type()函数创建的类和直接写class是完全一样的，
# 因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

# type()函数既可以返回一个对象的类型，又可以创建出新的类
