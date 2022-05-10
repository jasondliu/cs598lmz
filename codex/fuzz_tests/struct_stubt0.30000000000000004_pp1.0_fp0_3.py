from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update(Struct.__dict__)
s.format = '<3s3sHH'
print(s.size)

import struct
print(struct.calcsize('<3s3sHH'))

# 如果你想通过new方法来控制实例的创建，并且希望类的子类能继承它，可以在new方法中把类作为参数传递进去。
# 下面是一个例子：
import time
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year,
