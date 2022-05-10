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
Struct.__new__ is Struct.__new__

# __init__ is a plain instance method
Struct.__init__ is Struct.__init__

# __new__ is a static method (special-cased)
Struct.__new__ is Struct.__dict__['__new__']

# __init__ is a plain instance method
Struct.__init__ is Struct.__dict__['__init__']

# __new__ is a static method (special-cased)
Struct.__new__ is Struct.__class__
