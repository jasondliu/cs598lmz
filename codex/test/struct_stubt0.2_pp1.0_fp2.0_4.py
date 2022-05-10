from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# __new__ is a class method, so it is called on the class, not on the instance.
# The first argument to __new__ is the class, so we can use it to create an instance of the class.
# The second argument is the string that defines the format.
# The third argument is the endianness of the format.
# The fourth argument is the alignment of the format.

# The __init__ method is called on the instance, so it can use the instance attributes.
# The first argument to __init__ is the instance, so we can use it to set the instance attributes.
# The second argument is the string that defines the format.
# The third argument is the endianness of the format.
# The fourth argument is the alignment of the format.

# The pack method is called on the instance, so it can use the instance attributes.
# The first argument to pack is the instance, so we can use it to get the instance attributes.
# The second argument is the value to pack.

# The unpack method is called on the instance
