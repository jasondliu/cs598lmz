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
    pass

# __new__ can be overridden to customize creation
class VariableStruct(Struct):
    def __new__(cls, format, *args):
        return Struct.__new__(cls, format + 's')

s = VariableStruct.__new__(VariableStruct, 'i')
s.size

# __new__ is called when subclass is instantiated
class Point(Struct):
    _fields_ = [('x', 'i'), ('y', 'i')]

p = Point(42, 43)
p

# __new__ is called when subclass is instantiated
class Point(Struct):
    _fields_ = [('x', 'i'), ('y', 'i')]
