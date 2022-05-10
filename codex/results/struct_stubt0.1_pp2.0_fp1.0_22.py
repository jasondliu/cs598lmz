from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, so it is called without an instance of the class.
# It is called before __init__() and is used to return a new instance of the class.
# The __new__() method is useful for controlling the creation of a new instance.
# For example, you can use it to customize the way that instances are created.
# You can also use it to return a cached instance, instead of creating a new instance.
# The __new__() method is a static method, so it is called without an instance of the class.
# It is called before __init__() and is used to return a new instance of the class.
# The __new__() method is useful for controlling the creation of a new instance.
# For example, you can use it to customize the way that instances are created.
# You can also use it to return a cached instance, instead of creating a new instance.

# The __new__() method is a static method, so it is called without an instance of the class.
# It is called before __init__() and is
