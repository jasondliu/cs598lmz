from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# struct.Struct.__new__(format)
# Return a new Struct object which writes and reads binary data according to the format string format.
# The format string is composed of zero or more directives:
#
# Format	C Type	Python type	Standard size	Notes
# x	pad byte	no value
# c	char	bytes of length 1	1
# b	signed char	integer	1	(1),(3)
# B	unsigned char	integer	1	(3)
# ?	_Bool	bool	1	(1)
# h	short	integer	2	(3)
# H	unsigned short	integer	2	(3)
# i	int	integer	4	(3)
# I	unsigned int	integer	4	(3)
# l	long	integer	4	(3)
# L	unsigned long	integer	4	(3)
# q	long long	integer	8	(2), (
