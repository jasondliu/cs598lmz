from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.unpack(b'\x00\x00\x00\x00')

# 如果你想通过某个类创建实例，但是又不想调用 init() 方法，你可以使用 new() 方法来代替
# 例如，下面的代码使用 new() 来创建实例：
import time
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

# Create a new instance of Date
