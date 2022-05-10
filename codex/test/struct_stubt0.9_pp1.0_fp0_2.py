from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__('format', 'bhi')
s = s.__new__(Struct, '<bhi')
s.pack(1, 2, 3)
''.encode('latin-1')

class CBinding:

    def pack(self, *args):
        "Pack values according to this instance's format."
        return args

    def unpack(self, buf):
        "Return a tuple containing values unpacked according to this instance's format."
        return (1, 2, 3)

    def calcsize(self):
        "Return size in bytes of the struct representation of one instance of the format."
        return 3

    def iter_unpack(self, buf):
        "Generator yielding tuples containing values unpacked according to this instance's format."
        yield (1, 2, 3)

    def pack_into(self, buf, offset, *args):
        "Pack values according to this instance's format starting at specified offset in buffer."
        return offset

