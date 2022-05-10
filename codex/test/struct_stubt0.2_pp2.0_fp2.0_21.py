from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__.__get__(Struct) is Struct.__new__

# __new__ is a static method (special-cased)
Struct.__new__.__get__(s) is Struct.__new__

# __new__ is a static method (special-cased)
s.__new__ is Struct.__new__

# __new__ is a static method (special-cased)
s.__new__ is s.__class__.__new__

# __new__ is a static method (special-cased)
s.__new__(Struct) is s.__class__.__new__(Struct)

# __new__ is a static method (special-cased)
s.__new__(Struct, 'i') is s.__class__.__new__(Struct, 'i')

# __new__ is a static method (special-cased)
s.__new__(Struct, 'i').__class
