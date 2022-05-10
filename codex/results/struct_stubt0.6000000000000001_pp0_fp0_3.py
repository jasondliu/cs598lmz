from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('h')
s.unpack_from(b'\x00\x01', 2)
</code>
This is a bit of a hack, but it works.
You could also subclass Struct and create a <code>unpack_from</code> method that does what you want:
<code>class MyStruct(Struct):
    def unpack_from(self, buffer, index=0):
        return super().unpack_from(buffer, index)[0]

s = MyStruct('h')
s.unpack_from(b'\x00\x01', 2)
</code>

