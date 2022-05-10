from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('test')
s.format

class struct(Struct):
    def __init__(self, format):
        Struct.__init__(self, format)

    def __repr__(self):
        return "struct(%s)" % (self.format,)
