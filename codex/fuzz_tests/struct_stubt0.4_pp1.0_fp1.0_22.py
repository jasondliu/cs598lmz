from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
print(s.size)

# _struct.Struct.__new__() takes a format string, and returns a class that
# implements a binary data structure corresponding to the format string.
# The class has two methods: pack() and unpack(). The pack() method takes
# a sequence of values and returns a bytes object containing the values
# packed according to the format string. The unpack() method does the reverse:
# it takes a single bytes object (or a bytearray) and unpacks it according
# to the format string, returning a tuple of values.

# The format string is a sequence of characters that describe the layout
# of the binary data. Each character in the string corresponds to an item
# in the sequence passed to pack() or unpack(). The characters in the
# string have the following meaning:

# Format	C Type				Python type			Standard size
# x			pad byte			no value
# c			char				bytes of length 1	1
# b			signed char			integer			
