from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.unpack(data)

# 使用struct模块
import struct
struct.unpack('>I', data)

# 使用numpy模块
import numpy as np
np.frombuffer(data, dtype='>I')

# 使用memoryview
m = memoryview(data)
m.cast('I')

# 使用array模块
import array
array.array('I', data)

# 使用io模块
import io
io.BytesIO(data).read()

# 使用bitstring模块
import bitstring
bitstring.ConstBitStream(bytes=data).unpack('>I')

# 使用cffi模块
import cffi
ffi = cffi.FFI()
ffi.cast('uint32_t *', data)[0]

# 使用ctypes模
