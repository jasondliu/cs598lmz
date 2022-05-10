from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('QQQQQQQ', "little", False)
</code>
The bytes are the same in both cases:
<code>b'\xd2\x04\x00\x00\x05\x00\x00\x00'
</code>

