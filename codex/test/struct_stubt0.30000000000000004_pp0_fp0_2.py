from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("<i")
s.unpack(b"\x00\x00\x00\x00")

# 这个例子中，我们使用了 Struct 类的 __new__() 方法来创建一个新的实例。
# 这个方法的第一个参数是类本身，因此我们可以使用 Struct.__new__() 来创建一个新的结构对象。
# 然后，我们调用 __init__() 方法来初始化结构对象。
# 这种方式的一个主要缺点是它不能被继
