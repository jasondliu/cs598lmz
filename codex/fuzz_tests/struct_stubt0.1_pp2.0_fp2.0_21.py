from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__ is Struct

# __init__ is a plain instance method
Struct.__init__ is s.__init__

# __new__ is called without an instance of the class
Struct.__new__ is object.__new__

# __init__ is called with an instance of the class
Struct.__init__ is object.__init__

# __new__ is called first, and returns an instance of the class
Struct.__new__(Struct, 'i') is s

# __init__ is called on the instance returned by __new__
s.__init__ is Struct.__init__

# __new__ is called with the class as the first argument
Struct.__new__.__self__ is Struct

# __init__ is called with the instance as the first argument
s.__init__.__self__ is s

# __new__ is a static method
Struct.__new__.__func__ is Struct.__new__

# __
