from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.unpack(b'\x00\x00\x00\x01')

# 在Python中，把一个类的实例变量称为数据属性，而把一个类的方法变量称为方法。
# 在Python中，实例方法的第一个参数是self，而类方法的第一个参数是cls。
# 在Python中，类方法和静态方法都是通过装饰器实现的。
# 在Python中，类的实例可以调用类方法，类方法
