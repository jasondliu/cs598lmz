from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.unpack(b'\x01\x00\x00\x00')

# Result: (1,)

# 用户定义类
# 使用__new__方法创建对象
# 如果__new__返回一个cls类的实例，则调用__init__方法
# 如果__new__返回其他类型的实例，则不调用__init__方法
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

d = Date.__new__(Date)
data = {'year': 2012, 'month': 8, 'day': 29}
