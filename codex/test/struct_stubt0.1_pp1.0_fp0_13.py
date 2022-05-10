from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__(Struct, 'i')

# __new__ must return an instance of _struct
try:
    Struct.__new__(Struct, 'i', 42)
except TypeError:
    print('TypeError')

# __init__ is not called if __new__ returns an instance of _struct
class S(Struct):
    def __init__(self, format):
        print('__init__ called')

try:
    S.__new__(S, 'i')
except TypeError:
    print('TypeError')

# __new__ can return an instance of a subclass
class S(Struct):
    def __init__(self, format):
        print('__init__ called')

S.__new__(S, 'i')

# __new__ can return an instance of a different subclass
class S(Struct):
    def __init__(self, format):
        print('__init__ called')

