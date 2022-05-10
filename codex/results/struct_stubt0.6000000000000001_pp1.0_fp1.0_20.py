from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<h')
print s.size

# this is the same as
s = Struct('<h')
print s.size

# the format string is the first argument 
# to the Struct constructor.
# The format string describes the layout of the struct.
# It is a sequence of format characters
# each of which corresponds to a single struct field.
# The struct format characters are listed in Table 7-1.
# The first argument to Struct is a string containing the format
# The optional second argument is the endianness of the data
# in the struct.
# The default is native, which means that the native byte
# order is used.
# The optional third argument is a character indicating the
# alignment of the data in the struct.
# The default is @, which means that the data is aligned
# according to the native alignment requirements.
# The optional fourth argument is the error handler
# to be used when the format string is invalid.
# The default is Struct.error, which raises a struct.error
# exception.

# The struct module has a number of other functions that
# can be
