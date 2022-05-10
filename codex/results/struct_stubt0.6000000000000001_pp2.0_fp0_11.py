from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('h', 'big')
s.unpack(b'\x01\x00')
</code>
Output:
<code>(1,)
</code>

