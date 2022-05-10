from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__ is Struct

# __init__ is a normal instance method
Struct.__init__ is not Struct

# __init__ always returns None
Struct.__init__('i').__class__ is NoneType

# Calling the class is the same as calling __new__ followed by __init__
Struct('i').size == Struct.__new__(Struct).__init__('i').size

# Calling the instance is the same as calling __init__
# (except it returns self)
s = Struct('i')
s.size == s.__init__('i').size

# Calling the instance with a new format updates the instance in-place
# and returns None
s.__init__('i').__class__ is NoneType
s.size

# Calling the class with a new format creates a new instance
Struct('i').size == Struct('i').__new__(Struct).__init__('i').size

# Calling the class with a new format creates a
