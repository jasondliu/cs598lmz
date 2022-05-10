from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# 这里的结果是4，因为在32位机器上，一个整数占4个字节

# 如果要创建一个字节字符串，可以使用字节数组来构造，比如：

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
len(data)

# 这里的结果是16，因为每个字节都用两个十六进制的数字表示。

# 为了
