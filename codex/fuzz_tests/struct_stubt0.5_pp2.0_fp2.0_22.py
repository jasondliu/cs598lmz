from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(10)

# 使用__new__方法创建一个类，并且返回这个类的一个实例
# 类方法：cls表示类本身，是类方法的第一个参数
# 实例方法：self表示实例本身，是实例方法的第一个参数
# 类方法和实例方法的区别：类方法必须调用类方法，实例方法必须通过类的实例来调用

#
