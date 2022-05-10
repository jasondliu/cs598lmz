from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I')
s.unpack_from(data, 3)
(1268507536,)
</code>

