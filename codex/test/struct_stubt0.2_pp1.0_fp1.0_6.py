from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 在Python中，每个类都有一个__dict__属性，它是一个字典，用来存储实例的属性。
# 如果你自己定义了一个属性，那么它会被加入到__dict__中。
# 但是如果你是通过继承得到的属性，那么它就不会出现在__dict__中。
# 但是你可以通过dir()函数来查看所有的属性。
# 如果你想要
