from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update(Struct.__dict__)
s.format = '>I'
s.size = Struct.calcsize(s.format)
del Struct

HDR_SIZE = 16

# http://docs.python.org/3.3/library/struct.html#format-characters
# format character	C type	Python type	standard size						notes
# x	pad byte	no value																used for padding
# B	unsigned char	integer	1																	(3)
# H	unsigned short	integer	2																	(3)
# I	unsigned int	integer	4																		(3)
# Q	unsigned long long	integer	8																	(2), (3)
# s	char[]	
