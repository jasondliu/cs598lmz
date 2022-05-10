from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# 内建类型
# 内建类型是Python解释器内部实现的类型，它们和普通的类定义没有什么不同，也可以创建自己的实例，
# 但是内建类型的实例不能修改，比如不能添加新的属性。内建类型的实例都是不可变的，这意味着每次对它们进行操作时，
#
