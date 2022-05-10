from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# 这段代码的执行顺序如下：
# 1. 调用Struct.__new__方法创建一个空的结构体对象，并将其存储在s变量中。
# 2. 调用s.__init__方法初始化结构体对象，将格式字符串设置为'i'。
# 3. 调用s.pack方法将整数1打包为字节字符串。

# 打包数据
import struct
data = struct.pack('>i4sh', 7, b'spam', 8)
data

#
