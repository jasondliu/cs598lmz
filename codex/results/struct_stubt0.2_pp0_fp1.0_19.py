from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.unpack(b'\x00\x00\x00\x00')

# 这个例子中，我们使用 Struct.__new__() 来创建一个未初始化的结构对象。
# 然后，我们直接调用 __init__() 方法来初始化它。
# 这样做的好处是可以在 __init__() 方法中做一些额外的检查或者修改实例属性。

# 另外一个例子是，当你想要控制实例的创建过程
