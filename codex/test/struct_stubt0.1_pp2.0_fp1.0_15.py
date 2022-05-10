from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__(Struct, 'i')

# __new__ must return an instance of _struct
try:
    Struct.__new__(Struct, 'i').__new__(str)
except TypeError as e:
    print(e)

# __init__ is not called
try:
    Struct.__new__(Struct, 'i').__init__('d')
except TypeError as e:
    print(e)

# __new__ can be overloaded to customize instance creation
class Structure(Struct):
    def __new__(cls, *args):
        print('Creating a new instance')
        return super().__new__(cls, *args)

Structure('i')

# __new__ can be overloaded to customize instance creation
class Structure(Struct):
    def __new__(cls, *args):
        print('Creating a new instance')
        return super().__new__(cls, *args)

St
