from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('&gt;bbbbb')
s.unpack(bytearray([1,2,3,4,5]))
</code>

