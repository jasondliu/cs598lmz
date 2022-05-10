from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(">BBIiH")
s.pack(1, 2, 3, 4, 5)

# 使用__new__创建一个类，并且在__init__中填充一些属性
class Date:
    __slots__ = ["year", "month", "day"]
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

class Date:
    __slots__ = ["_year", "_month", "_day"]
    def __init__(self, year, month, day):
        self._year = year
        self._month = month
        self._day = day
    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, value):
        self._year = value
    @property
    def month(self):
        return self._month
