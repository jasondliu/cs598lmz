from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('', '12s')
s.unpack(b'abcdefghijkl')
('abcdefghijkl',)
</code>

