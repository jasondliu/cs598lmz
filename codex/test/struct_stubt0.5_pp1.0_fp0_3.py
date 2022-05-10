from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# __new__()方法接受一个参数cls，代表要实例化的类，它总是会返回当前类的一个实例，因此在__new__()方法中就可以改变当前类的实例
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return '%04d-%02d-%02d' % (self.year, self.month, self.day)

    @classmethod
    def today(cls):
        t = localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_day)


