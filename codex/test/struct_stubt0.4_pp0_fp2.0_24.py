from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# A simple example of using __new__
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __new__(cls, year, month, day):
        if month > 12 or month < 1 or day < 1 or day > 31:
            raise ValueError('Invalid date')
        return object.__new__(cls)

# A simple example of using __new__ and __init__
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __new__(cls, year, month, day):
        if month > 12 or month < 1 or day < 1 or day > 31:
            raise ValueError('Invalid date')
        return object.__new__(cls)

