from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

import struct
st = struct.Struct('i')
st.size

# 下面是一个简单的示例，它使用 struct 库将数据编码到二进制数组中：
import struct

values = (1, 'ab'.encode('utf-8'), 2.7)
s = struct.Struct('I 2s f')
packed_data = s.pack(*values)

# 使用 unpack() 方法将这些数据重新解压缩：
import struct

packed_data = b'0100000061620000cdcc2c40'
s = struct.Struct('I 2s f')
unpacked_data = s.unpack(packed_data)
unpacked_data

