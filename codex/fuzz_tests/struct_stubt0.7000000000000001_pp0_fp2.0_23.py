from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('@H')
s.size

# 结构体格式的字母如下所示
# Format	C Type	    Python type	    Standard size	Notes
# x	        pad byte	no value
# c	        char	    string of length 1	1
# b	        signed char	integer	            1
# B	        unsigned char	integer	        1
# ?	        _Bool	    bool	            1	        (see note)
# h	        short	    integer	            2
# H	        unsigned short	integer	    2
# i	        int	        integer	            4
# I	        unsigned int	integer	        4
# l	        long	    integer	            4
# L	        unsigned long	integer	        4
# q	        long long	integer	            8
# Q	        unsigned long long	integer	    8
# f	        float	    float	            4
# d	        double	    float	            8
# s	        char
