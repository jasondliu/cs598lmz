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

# __new__ can return a different class
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

class NewDate(Date):
    def __new__(cls, year, month, day):
        if year > 2000:
            cls = Date
        return super().__new__(cls)

d = NewDate(2050, 12, 31)
d.year

# __new__ can return an instance
