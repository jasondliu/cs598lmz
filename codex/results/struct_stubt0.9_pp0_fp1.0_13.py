from _struct import Struct
s = Struct.__new__(Struct)
s.format = '&lt;li'
s.size = ctypes.sizeof(data)
data = data.tobytes()
s.unpack_from(data, 10)
</code>

