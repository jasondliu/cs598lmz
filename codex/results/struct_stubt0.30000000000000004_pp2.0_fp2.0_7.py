from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<3s3sHH'
s.size = calcsize(s.format)
print(s.size)

# 用户定义的类可以实现 __new__ 方法，这样就可以在实例化时自定义对象的创建过程。
# 例如，下面的代码定义了一个能控制实例化过程的类：
import time
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.
