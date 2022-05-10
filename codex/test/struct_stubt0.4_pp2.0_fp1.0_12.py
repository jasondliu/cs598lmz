from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

# 可以看出，当我们调用Struct对象的__init__方法时，第一个参数是一个格式字符串，由多个格式符号组成，每个格式符号代表一种C结构成员的类型。
# 可以用来表示的格式符号包括：
#
# 符号	C类型	Python类型	尺寸
# x	pad byte	no value
# c	char	bytes of length 1	1
# b	signed char	integer	1
# B	unsigned char	integer	
