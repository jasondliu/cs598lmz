from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'bB'
s.size = s.calcsize()

def s_unpack(data):
    "Unpack from the front of the data buffer"
    return s.unpack(data)

def s_pack(data, *values):
    "Pack values and append to the end of the data buffer"
    return s.pack(_data, *values)
</code>
And to use, just do something like:
<code>data = io.BytesIO()
s_pack(data, 0xab, 0x33, 0xff, 0xee)
# data.getvalue() returns '\xab\x33\xff\xee'
foo, bar, baz, qux = s_unpack(data.getvalue())
</code>
Where <code>foo == 0xab, bar == 0x33, baz == 0xff and qux == 0xee</code>.

