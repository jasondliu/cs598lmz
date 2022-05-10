from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# 如果你不想使用 __new__() 方法，你可以使用一个类工厂函数来代替。比如：
import time

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 下面是一个类方法，用来构造一个类实例
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

# 下面是使用类方法的例子
a = Date(2012, 12, 21)
b = Date
