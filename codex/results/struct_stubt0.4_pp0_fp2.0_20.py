from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, so it is called without an instance.
# It returns an instance of the class.

# In this example, the class is Struct, and the instance is s.

# The size of the struct format is determined by the format string.

# The struct module can be used to interpret binary data.

# The struct module has a Struct class.

# The __init__() method of the Struct class takes a format string.

# The size of the struct format is determined by the format string.
