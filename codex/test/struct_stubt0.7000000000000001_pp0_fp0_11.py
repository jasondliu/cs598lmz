from _struct import Struct
s = Struct.__new__(Struct)
s.format = "=hhl"
s.size = s.calcsize(s.format)
s.unpack = s.__call__(s.format)

for i, line in enumerate(open('./data/tiny.txt')):
    data = line.rstrip('\n')
