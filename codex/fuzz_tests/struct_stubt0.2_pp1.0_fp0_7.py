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

# __new__ can be used to control instance creation
class VariableStruct(Struct):
    def __new__(cls, format):
        self = Struct.__new__(cls, format)
        self.format = '!' + format
        return self

vs = VariableStruct('i')
vs.format
vs.size

# __new__ can be used to change instance creation
class VariableStruct(Struct):
    def __new__(cls, format):
        self = Struct.__new__(cls, '!' + format)
        self.format = format
        return self

vs = VariableStruct('i')
vs.format
vs.size

# __new__ can be used to change instance creation
class VariableStruct(Struct
