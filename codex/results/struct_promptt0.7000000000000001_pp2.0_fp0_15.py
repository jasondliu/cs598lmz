import _struct
# Test _struct.Struct

import struct

# struct.pack(fmt, v1, v2, ...) --> string
# struct.unpack(fmt, string) --> (v1, v2, ...)
# struct.calcsize(fmt) --> int

# Format	C Type			Python Type 		Standard size
# x		pad byte 		no value		1
# c		char			string of length 1	1
# b		signed char		integer			1
# B		unsigned char		integer			1
# ?		_Bool			bool			1
# h		short			integer			2
# H		unsigned short		integer			2
# i		int			integer			4
# I		unsigned int		integer			4
# l		long			integer			4
# L		unsigned long		integer			4
# q		long long		integer			8
# Q		unsigned long long
