from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, so it is called on the class, not on an instance.
# It is called before __init__() and is passed the class itself as the first argument.
# Its job is to return a new instance of that class.
# In this example, the class is Struct, and the new instance is s.
# The __init__() method is then called on the new instance, with the remaining arguments.
# Its job is to initialize the instance.
# In this example, it initializes the format attribute of the instance.
# The size attribute is then computed from the format string.

# The __new__() method is rarely used in Python code.
# It is used when you want to control the creation of a new instance.
# For example, you might want to return a cached instance, or you might want to return a subclass.
# In this case, you would override __new__() and create the new instance there.
# The __init__() method is more commonly used.
# It is called after the instance has been created, and is used
