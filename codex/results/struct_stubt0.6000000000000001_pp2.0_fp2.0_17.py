from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(">I")
s.size

# struct.pack(fmt, v1, v2, ...)
# fmt -- 格式字符串
# v1, v2, --  可选的值

# struct.pack_into(fmt, buffer, offset, v1, v2, ...)

# struct.unpack(fmt, string)
# struct.unpack_from(fmt, buffer, offset=0)

# fmt -- 格式字符串
# buffer -- 可选，缓冲区
# offset -- 可选，默认为 0
# string -- 要解包的字符串

# 格式字符串
# 格式字符串由空格分隔的标记组成，
