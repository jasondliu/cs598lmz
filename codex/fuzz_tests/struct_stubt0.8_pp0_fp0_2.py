from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'IHH'

data = open(sys.argv[1]).read()

for i in range(0, len(data), struct.calcsize(s.format)):
    d = s.unpack_from(data, i)
    print d
