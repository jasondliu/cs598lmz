import _struct

class _Struct(object):
    def __init__(self, fmt):
        self.fmt = fmt
        self.size = struct.calcsize(fmt)

    def pack(self, *args):
        return struct.pack(self.fmt, *args)

    def unpack(self, data):
        return struct.unpack(self.fmt, data)

    def unpack_from(self, data, offset=0):
        return struct.unpack_from(self.fmt, data, offset)


class _StructField(object):
    def __init__(self, fmt, offset):
        self.fmt = fmt
        self.offset = offset

    def _pack(self, value):
        return struct.pack(self.fmt, value)

    def _unpack(self, data):
        return struct.unpack(self.fmt, data)

    def _unpack_from(self, data, offset=0):
        return struct.unpack_from(self.fmt, data, offset)


