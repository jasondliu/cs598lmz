from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.pack(1)

# 使用__new__方法创建类的实例
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

d = Date.__new__(Date)
data = {'year': 2012, 'month': 8, 'day': 29}
for key, value in data.items():
    setattr(d, key, value)
d.year

# 创建不可变的类型
class Date:
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

d = Date(2012, 12, 21)
d.year = 2013

# 使用__slots__定义的属
