from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('iframe_header', '>hiq')

with open(sys.argv[1], 'rb') as f:
    data = f.read(s.size)
    print('type', s.unpack_from(data)[0])
    print('size', s.unpack_from(data)[1])
    print('time', s.unpack_from(data)[2])
