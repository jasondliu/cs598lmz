import _struct

class Struct(object):
    def __init__(self, fmt):
        self.fmt = fmt
        self.size = _struct.calcsize(fmt)

    def pack(self, *args):
        return _struct.pack(self.fmt, *args)

    def unpack(self, data):
        return _struct.unpack(self.fmt, data)

class StructField(object):
    def __init__(self, fmt, offset):
        self.format = fmt
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            r = _struct.unpack_from(self.format, instance._buffer, self.offset)
            return r[0] if len(r) == 1 else r

    def __set__(self, instance, value):
        if not isinstance(value, tuple):
            value = (value, )
        _struct.pack_into(self.format, instance._buffer, self.offset, *value)

