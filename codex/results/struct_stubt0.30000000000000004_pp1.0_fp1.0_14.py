from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.unpack(b'\x00\x00\x00\x01')

# 使用struct模块的pack函数打包，使用unpack函数解包
# pack的第一个参数是处理指令，'>I'的意思是：>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
# 后面的参数个数要和处理指令一致。
import struct
struct.pack('>I', 10240099)

# unpack把bytes变成相应的数据类型
