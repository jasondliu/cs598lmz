import _struct

#
#
#
class _struct_fmt(object):
    def __init__(self, fmt):
        self.fmt = fmt
        self.size = _struct.calcsize(fmt)
    def pack(self, *args):
        return _struct.pack(self.fmt, *args)
    def unpack(self, *args):
        return _struct.unpack(self.fmt, *args)

#
#
#
class _struct_fmt_str(object):
    def __init__(self, fmt):
        self.fmt = fmt
        self.size = _struct.calcsize(fmt)
    def pack(self, *args):
        return _struct.pack(self.fmt, *args)
    def unpack(self, *args):
        return _struct.unpack(self.fmt, *args)[0]

#
#
#
