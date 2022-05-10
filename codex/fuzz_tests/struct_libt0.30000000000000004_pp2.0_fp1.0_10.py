import _struct

#
# 
#
class _CStruct(object):
    """
    """
    def __init__(self, fmt, data):
        self.fmt = fmt
        self.data = data

    def __getattr__(self, name):
        """
        """
        offset = self.fmt.offset(name)
        if offset is None:
            raise AttributeError("%s has no attribute %s" % (self.__class__.__name__, name))
        return _struct.unpack_from(self.fmt.fmt[offset], self.data, offset)[0]

    def __setattr__(self, name, value):
        """
        """
        if name in ("fmt", "data"):
            self.__dict__[name] = value
            return
        offset = self.fmt.offset(name)
        if offset is None:
            raise AttributeError("%s has no attribute %s" % (self.__class__.__name__, name))
        _struct.pack_into(self.f
