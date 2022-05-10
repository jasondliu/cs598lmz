from _struct import Struct
s = Struct.__new__(Struct)
s.format = '10s1s1s1s1s1s'
s.size = calcsize(s.format)

with open(sys.argv[1], 'rb') as f:
    while True:
        buf = f.read(s.size)
        if len(buf) == 0:
            break
        if len(buf) != s.size:
            raise Exception("File size mismatch")
