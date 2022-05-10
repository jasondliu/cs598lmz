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

# __new__ can customize creation
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

a = Date(2012, 12, 21)
b = Date.today()

# __new__ can return an instance of a different
