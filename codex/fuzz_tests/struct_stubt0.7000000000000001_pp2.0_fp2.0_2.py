from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('L', 'L')
s.pack(1000000000000, 2000000000000)
</code>

