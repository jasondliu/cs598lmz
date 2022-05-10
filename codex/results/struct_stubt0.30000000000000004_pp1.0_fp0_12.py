from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.unpack(b'\x00\x00\x00\x01')

# 所以，在Python中，每个类都有一个__dict__属性，用来存储一个类的成员；
# 每个对象也有一个__dict__属性，用来存储一个对象的成员。
# 但是，类的__dict__属性存储的是类的成员，而实例的__dict__属性存储的是实例的成员。
# 所以，如果你在一个实例上添加一
