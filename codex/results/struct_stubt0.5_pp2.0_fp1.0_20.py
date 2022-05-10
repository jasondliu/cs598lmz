from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.unpack(b'\x00\x00\x00\x01')

# 如果你真的需要通过一个类去控制实例的创建过程，可以在一个类中定义一个
# __new__() 方法，比如下面这个例子：
import time
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __new__(cls, *args, **kwargs):
        print('__new__() is called.')
        if len(args) == 0:
            t = time.localtime()
            args = (t.tm_year, t.tm_mon, t.tm_mday
