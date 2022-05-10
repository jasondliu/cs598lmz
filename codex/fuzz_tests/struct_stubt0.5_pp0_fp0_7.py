from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('hhl')
s.size

# _struct.Struct.__new__(format)
# 创建并返回一个新的Struct对象。format参数用于指定所需的C结构的格式。
# 如果没有提供format参数，则默认为'x'，它将导致unpack()始终返回一个空字节字符串。
# 如果提供了format参数，则它必须是一个字符串，其中每个字符都指定了一个C结构字段的
