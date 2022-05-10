from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 可以用一个类模拟其他类的实例。为此，你需要定义一个特殊的__call__()方法，
# 就像下面这样：
import time

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __call__(self):
        return (self.year, self.month, self.day)

date = Date(2012, 12, 21)
date()

# 为了模拟一个简单的对象，你可以使用一个普通的实例。
# 但是，
