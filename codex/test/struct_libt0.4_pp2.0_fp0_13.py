import _struct

class _Cdata:
    def __init__(self, value, type):
        self.value = value
        self.type = type
    def __repr__(self):
        return '<Cdata %s %s>' % (self.type, self.value)
    def __int__(self):
        return self.value

class _Ctype:
    def __init__(self, name, size, alignment, pack, unpack, format):
        self.name = name
        self.size = size
        self.alignment = alignment
        self.pack = pack
        self.unpack = unpack
        self.format = format
    def __repr__(self):
        return '<Ctype %s>' % self.name

def _Ctype_new(name, size, alignment, pack, unpack, format):
    return _Ctype(name, size, alignment, pack, unpack, format)

def _Ctype_new_primitive_type(name, size, alignment, pack, unpack, format):
    return _C
