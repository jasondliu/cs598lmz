from _struct import Struct
s = Struct.__new__(Struct)
s.format = '&lt;hhI'
s.size = struct.calcsize(s.format)
def unpack_from(self, buffer, offset=0):
    values = struct.unpack_from(self.format, buffer, offset)
    return values
s.unpack_from = unpack_from
s.unpack_from(data,16)
(1, 2, 3)
</code>
For the record...
<code>info = {'count': 1,
        'method': 'PACKBITS',
        'width': 2048,
        'height': 1536,
        'planes': 1,
        'bits': 16,
        'raw_info': (1, 2, 3),
        'extra': []}
</code>

