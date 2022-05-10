from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('&lt;i')

def read_int(f):
    return s.unpack(f.read(4))[0]
</code>

