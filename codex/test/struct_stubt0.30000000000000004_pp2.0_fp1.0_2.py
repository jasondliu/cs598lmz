from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.unpack(b'\x00\x00\x00\x00')

# 如果你想通过某个类创建实例，但是又不想调用 init() 方法，那么你可以使用 new() 方法
# 这个方法在继承元组的时候很有用
# 例如，下面这个类被设计用来作为一个字节存储单元，它的行为就像一个元组，但是每个字段都有名称
