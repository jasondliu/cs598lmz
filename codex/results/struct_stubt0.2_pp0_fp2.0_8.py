from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__(Struct, 'i')
Struct.__new__(Struct, 'i').size

# __new__ must return an instance of _struct
try:
    Struct.__new__(Struct, 'i', 42)
except TypeError:
    print('TypeError')

# __new__ is called even if there is no __init__
class S(Struct):
    def __init__(self, *args):
        raise TypeError
S.__new__(S, 'i')

# __new__ can be overridden without affecting __init__
class S(Struct):
    def __new__(cls, *args):
        print('S.__new__', args)
        return Struct.__new__(cls, *args)
    def __init__(self, *args):
        print('S.__init__', args)
S('i')

# __new__ can be overridden without affecting __init__
class
