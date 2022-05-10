import _struct

# This is a simplified version of the struct module that is only
# capable of unpacking data.

# Format	C Type			Python type			Standard size
# x		pad byte		no value
# c		char			string of length 1		1
# b		signed char		integer				1
# B		unsigned char		integer				1
# ?		_Bool			bool				1
# h		short			integer				2
# H		unsigned short		integer				2
# i		int			integer				4
# I		unsigned int		integer				4
# l		long			integer				4
# L		unsigned long		integer				4
# q		long long		integer				8
# Q		unsigned long long	integer				8
# f		float			float				4
# d		double
