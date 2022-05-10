from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, so it is called on the class, not on an instance.
# It is called before __init__() and is passed the class itself as the first argument.
# Its job is to return a new instance of that class.
# In this case, the class is Struct, and the new instance is a Struct object.
# The __init__() method is then called on the new instance,
# and it initializes the instance by saving the format string.
# The size attribute is then computed by calling calcsize() on the format string.

# The __new__() method is rarely used in Python code,
# but it is used in the implementation of immutable types like int, str and tuple.
# It is also used in the implementation of singletons.
# Singletons are classes that have only one instance.
# For example, logging.Logger is a singleton.
# There is only one instance of Logger, and it is created the first time it is needed.
# The __new__() method is used to ensure that only one
