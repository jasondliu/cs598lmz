from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>i'
s.size = 4
s.pack(3)

# This is equivalent to the following
s = Struct('>i')
s.pack(3)


# The Struct class provides a number of other methods, such as the unpack method, which unpacks a packed data sequence 
# according to the format:

s = Struct('>i')
packed_data = s.pack(3)
s.unpack(packed_data)
(3,)


# The Struct class has a number of additional methods that provide more advanced functionality, such as the ability to 
# read and write data to files. See the documentation for details.

# Structs in the real world

# The struct module is most commonly used in situations where there is some preexisting data format that you have to 
# deal with. For example, if you want to parse data from a network packet, the struct module is a good choice.
# For example, suppose you want to parse a BMP file and read some meta information from the header. 
# A BMP file starts with a 54-byte header followed by
