import _struct
# Test _struct.Struct
endianness = {'@': 'native, native',
    '=': 'native, standard',
    '<': 'little-endian',
    '>': 'big-endian',
    '!': 'network (= big-endian)'}
import sys
sys.byteorder
_struct.calcsize('Pi')
_struct.calcsize('Pii')
_struct.pack('ii', 1, 2)
_struct.unpack('ii', '\x00\x00\x00\x01\x00\x00\x00\x02')
# Test _struct.Struct
class S(_struct.Struct):
    def __init__(self, format):
        _struct.Struct.__init__(self, format)
        self.size = self.size

    def unpack(self, s):
        return _struct.Struct.unpack(self, s)

    def pack(self, *args):
        return _struct.Struct.pack(self, *args)
S._formats_supported = _struct.Struct._formats_supported.copy()
