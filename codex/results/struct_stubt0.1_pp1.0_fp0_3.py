from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__ is s.__new__

# __init__ is a plain instance method
Struct.__init__ is s.__init__

# __new__ is a static method (special-cased)
Struct.__new__ is s.__new__

# __init__ is a plain instance method
Struct.__init__ is s.__init__

# __new__ is a static method (special-cased)
Struct.__new__ is s.__new__

# __init__ is a plain instance method
Struct.__init__ is s.__init__

# __new__ is a static method (special-cased)
Struct.__new__ is s.__new__

# __init__ is a plain instance method
Struct.__init__ is s.__init__

# __new__ is a static method (special-cased)
Struct.__new__ is s.__new__

# __init__ is a plain instance
