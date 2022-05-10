from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# __new__ is a class method, so it is called on the class, not the instance
# __new__ is called before __init__
# __new__ can return any object, not necessarily an instance of the class
# __new__ is the right place to do metaclass programming

# __init__ is called after __new__
# __init__ is called on the instance
# __init__ is the right place to do instance programming

# __new__ is called on the class
# __init__ is called on the instance

# __new__ is called before __init__
# __init__ is called after __new__

# __new__ can return any object, not necessarily an instance of the class
# __init__ is called on the instance

# __new__ is the right place to do metaclass programming
# __init__ is the right place to do instance programming

# __new__ is the right place to do metaclass programming
# __init__ is the right place to do instance programming

# __new__ is the right
