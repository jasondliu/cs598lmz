from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# __new__() is a static method, so it is called without an instance of the class.
# It returns a new instance of the class.
# __init__() is an instance method, so it is called with an instance of the class.
# It initializes the instance.

# __new__() is called first, and is responsible for returning a new instance of your class.
# In contrast, __init__() is called after __new__(), and is responsible for initializing the instance.
# If you do not implement __new__(), the default implementation of object.__new__() is used.
# If you do not implement __init__(), nothing happens.

# The most common use for overriding __new__() is to return an instance of a subclass,
# instead of the base class.

# __new__() is called before __init__().
# __new__() is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class.
# In contrast, __init__() is the second step of
