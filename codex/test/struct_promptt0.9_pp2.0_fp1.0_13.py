import _struct
# Test _struct.Struct if it is available.
if hasattr(_struct, "Struct"):
    class byte_struct(object):
        __slots__ = ("bytesize", "format_code")

        def __init__(self, format_code):
            self.format_code = format_code
            self.bytesize = _struct.calcsize(self.format_code)

        def pack(self, x):
            return _struct.pack(self.format_code, x)

        def unpack(self, data):
            return _struct.unpack(self.format_code, data)[0]

    unpack_doubleword = byte_struct("<L").unpack

# otherwise...
else:
    def unpack_doubleword(data):
        return long(data[0]) + (long(data[1]) * 256) + (long(data[2]) * 65536) + (
            long(data[3]) * 16777216
        )

