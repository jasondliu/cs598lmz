from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# __new__() is a class method, so it is called on the class, not on an instance.
# It is called before __init__(), and it is the method that creates the instance and returns it.
# In the example above, the class method is called on Struct, and returns an instance of Struct.
# The instance is then passed to __init__(), which initializes it.

# __new__() is the right place to do metaclass customization.
# For example, if you want to return a specialized instance instead of the usual one,
# you can override __new__() to do that.

# The first argument passed to __new__() is the class it was called on.
# In the example above, this is Struct.
# The remaining arguments are the same as the arguments passed to __init__().
# In the example above, this is the format string '>i'.

# __new__() is also the right place to enforce constraints on the arguments passed to the class constructor.
# For example, if you want to ensure that the format string passed to
