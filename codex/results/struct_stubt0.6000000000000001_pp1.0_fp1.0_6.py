from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('hi')
s.pack(1,2)

#
# 没有给出格式字符串，缺省为 '>'
#
s = Struct()
s.pack(1,2)

#
# 只给出一个格式字符串，缺省的第一个字符是 '>'
#
s = Struct('i')
s.pack(1)

#
# 给出的格式字符串只有一个字符，它不是 '@' 或 '='，缺省的第一个字符是 '>'
#
s = Struct('i')
s.pack(1)

#
# 给出的格式字符串只有
