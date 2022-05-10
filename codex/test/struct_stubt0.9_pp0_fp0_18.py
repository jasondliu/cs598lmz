from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i', 0)
s

#______________________________________________________________________
class Struct:
    def __init__(self, format, *args): pass
    def __new__(cls, *args, **kwargs):
        if cls is Struct:
            raise TypeError("Struct is abstract")
        self = super(Struct, cls).__new__(cls)
        return self

print(Struct('i'))
