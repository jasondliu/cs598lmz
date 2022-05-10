from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# __new__ is a classmethod, and it returns an instance of the class
# __init__ is an instance method, and it initializes the instance
# __new__ is called before __init__
# __new__ can return an instance of a different class
# __init__ is called after __new__
# __init__ is called with the instance returned by __new__
# __new__ is called with the class it is defined in
# __init__ is called with the class it is defined in
# __new__ is called with the arguments passed to the class
# __init__ is called with the arguments passed to the class
# __new__ can return an instance of a different class
# __init__ is called with the instance returned by __new__
# __new__ is called with the arguments passed to the class
# __init__ is called with the instance returned by __new__
# __new__ is called with the arguments passed to the class
# __init__ is called with the instance returned by __new__
# __new__ can return an instance of a different
