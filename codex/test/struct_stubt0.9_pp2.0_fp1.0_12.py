from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
f = open(path)
ch = f.read(4)
un = s.unpack(ch)
