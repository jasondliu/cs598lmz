from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.unpack(b'\x00\x00\x00\x00')

# 可以用一个类来模拟其他类的实例
# 先定义底层的类
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

# 定义代理类
class DateTime(Date):
    def __init__(self, year, month, day, hour, minute, second):
        Date.__init__(self, year, month, day)
        self.hour = hour
        self.minute = minute
        self.second = second

# 代理类实例
a = DateTime(2012, 12, 21, 10, 11, 12)

# 代理类的实例
