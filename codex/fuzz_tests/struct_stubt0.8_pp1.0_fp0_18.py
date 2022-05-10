from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'bbccccc'
s.error = None
s.size = ctypes.sizeof(s.format)
</code>
but the <code>size</code> attribute is always <code>0</code>.

