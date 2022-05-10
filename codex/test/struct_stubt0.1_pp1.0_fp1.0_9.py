from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 可以使用类来创建实例，但是通常不这么做
# 因为类本身就是创建实例的元数据
# 使用类创建实例的一个主要用途是元编程
# 元编程就是利用程序来创建程序

# 使用元类
# 元类就是用来创建类的类
# type是Python内置的元类
# 元类的实例就是类
# 元类的实
