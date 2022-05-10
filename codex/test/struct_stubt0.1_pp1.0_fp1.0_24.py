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
Struct.__new__(Struct, 'i')

# __init__ is a plain instance method
Struct().__init__('i')

# __new__ is a static method (special-cased)
Struct.__new__(Struct, 'i').size

# __init__ is a plain instance method
Struct().__init__('i').size

# __new__ is a static method (special-cased)
Struct.__new__(Struct, 'i').size == Struct().__init__('i').size

