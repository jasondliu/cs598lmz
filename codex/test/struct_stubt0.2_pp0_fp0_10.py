from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.pack(1)

# 在Python中，每个类都有一个__dict__属性，用来存储实例的属性。
# 如果你定义了一个__slots__属性，那么Python就不会再为你的类创建__dict__属性了。
# 如果你还想要让实例能够保存属性，你需要把__slots__定义成一个可以接受属性名称的可迭代对象，比如列表或元组。
