from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

# _struct.Struct.__new__() takes a format string as its first argument,
# and returns a new subclass of Struct ready to accept packed data
# according to the given format.

# The format string uses the same syntax as the struct module.

# The resulting class defines __init__() and __len__() methods, and
# the class methods from_buffer() and from_buffer_copy()
# (see below).

# It also defines a __format__() method which returns the format string
# passed to __new__().

# The resulting class is callable, and takes a buffer argument which
# is used as the underlying memory for the instance.

# The buffer must contain exactly the right number of bytes
# for the format used, or struct.error will be raised.

# The optional first argument to the class is a buffer used to
# hold the instance data.

# If present, this must be an object supporting the buffer API.

# If omitted, a bytearray of the appropriate size will be created.

#
