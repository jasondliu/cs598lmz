from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>2s3si')

data = open('data.bin', 'rb').read()
print(s.unpack(data))
