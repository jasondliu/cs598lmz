from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__ is s.__new__

# __init__ is a plain instance method
Struct.__init__ is s.__init__

# __new__ is a static method (special-cased)
Struct.__new__ is Struct().__new__

# __init__ is a plain instance method
Struct.__init__ is Struct().__init__

# __new__ is a static method (special-cased)
Struct.__new__(Struct, 'i') is Struct('i')

# __init__ is a plain instance method
Struct('i').__init__('i') is Struct('i')

# __new__ is a static method (special-cased)
Struct.__new__(Struct, 'i') is Struct.__new__(Struct, 'i')

# __init__ is a plain instance method
Struct('i').__init__('i') is Struct('i').__init__('i')

# __new__ is
