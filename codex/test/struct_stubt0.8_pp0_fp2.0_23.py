from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.pack(1, b'ab', 2.7)

# 创建一个buffer
import array
nums = array.array('i', [1, 2, 3, 4])
s.pack_into(buffer, 0, 1, b'ab', 2.7)

# 将结构体打包的内容解析为一个元组
