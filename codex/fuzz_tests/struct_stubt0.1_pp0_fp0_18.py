from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__ is Struct

# __init__ is a plain instance method
Struct.__init__ is s.__init__

# __new__ is called first
class Spam:
    def __new__(cls):
        print('Creating instance')
        return super().__new__(cls)
    def __init__(self):
        print('Initializing instance')

s = Spam()

# __new__ can customize instance creation
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __new__(cls, year, month, day):
        if month > 12 or day > 31:
            raise ValueError('Invalid date: {}/{}/{}'.format(year, month, day))
        return super().__new__(cls)

d = Date(2018, 12, 31)


