from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('hif')
s.size

s.pack(1, 2.0, 3)
</code>

