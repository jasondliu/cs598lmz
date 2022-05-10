from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.unpack(b'\x00\x00\x00\x01')

# 在Python中，每个类都有一个__dict__属性，它是一个字典，用来存储实例的变量。
# 你可以通过__dict__属性来访问实例变量。
# 但是，你不应该直接访问__dict__属性，而应该使用实例的__getattr__()和__setattr__()方法。

# 如果你想要实现一个自定义容器，你可以继
