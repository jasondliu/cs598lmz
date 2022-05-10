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

# __new__ returns an instance of the class
Struct.__new__(Struct, 'i')
isinstance(_, Struct)

# __init__ returns None
Struct.__init__(s, 'i') is None

# __new__ is called at most once per instance
s1 = Struct('i')
s2 = Struct('i')
s1 is s2

# __init__ is called every time __new__ is called
s1 = Struct('i')
s2 = Struct('i')
s1.__init__ is s2.__init__

# __new__ can return an instance
