from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 创建一个类似的结构，并将其用作模板
import time
class DT(object):
    _fmt = '>I'
    def __init__(self, year, month, day, hour=0, minute=0, second=0):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    def __iter__(self):
        return (getattr(self, n) for n in self._fields)
    def __str__(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', self)
    @classmethod
    def now(cls):
        t = time.localtime()
        return cls
