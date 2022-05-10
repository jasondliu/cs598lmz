from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('hhl', byteorder='little', repr=True)
s.size

#解析
#_struct.unpack(fmt, string)
#将编码后的字符串解析为原始Python值
#_struct.unpack_from(fmt, buffer[, offset=0])
#将编码后的字符串解析为原始Python值(offset指定起始位置)

#pack_into()和pack(),unpack_from()和unpack()
#pack_into()和unpack_from()使用一个已存在的字符串来存储结果,而pack()和unpack()使用一个新分配的字符串
