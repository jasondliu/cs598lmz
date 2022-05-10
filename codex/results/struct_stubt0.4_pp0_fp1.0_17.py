from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

# _struct.Struct.unpack(s, data)
# _struct.Struct.pack(s, v1, v2, v3)

# struct.pack('>I', 10240099)
# struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

# struct.iter_unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

# with open('myfile.zip', 'rb') as f:
#     data = f.read()
#
# start = 0
# for i in range(3):                      # show the first 3 file headers
#     start += 14
#     fields = struct.unpack('<IIIHH', data[start:start+16])
#     crc32, comp_size, uncomp_size, filenamesize, extra_size = fields
#
#     start += 16
#     filename = data[start:start+fil
