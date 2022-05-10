from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x00\x00\x00\x00')

# 如果你想要通过某个类来控制实例的创建过程，可以在一个特殊的 __new__() 方法中实现这个目的。
# 下面是一个例子，它确保每次创建实例的时候都会被标记为“创建”状态：
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

