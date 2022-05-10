from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__ is Struct

# __init__ is a plain instance method
Struct.__init__ is s.__init__

# __new__ is called without an instance of the class
Struct.__new__(Struct, 'i')

# __init__ is called with an instance of the class
Struct.__init__(s, 'i')

# __new__ returns an instance of the class
Struct.__new__(Struct, 'i')

# __init__ returns None
Struct.__init__(s, 'i')

# __new__ is called first
Struct.__new__(Struct, 'i')

# __init__ is called second
Struct.__init__(s, 'i')

# __new__ can return a subclass
class SubStruct(Struct):
    pass

SubStruct.__new__(SubStruct, 'i')

# __init__ is still called on the class it was defined in
Struct.__init__
