from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 可以用一个类替换多个全局函数，比如，下面的代码就把 time.strftime() 和 time.localtime() 这两个函数绑定到了同一个类的实例上：
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

    def __str__(self):
        return '{}-{}-{}'.format(self.year, self.month, self.day)


